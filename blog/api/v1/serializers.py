from rest_framework import serializers
from ...models import Post, Category, Comment
from accounts.models import Profile

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "post", "parent", "user", "content",]
        read_only_fields = ["post", "user",]
    
    def validate_parent(self, value):
        if value.parent.parent is not None:
            raise serializers.ValidationError(
                "You cannot reply to a comment with depth of more then two."
            )
        return value
    
    


class PostSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    # content = serializers.ReadOnlyField() or --> content = serializers.CharField(read_only=True)
    # category = CategorySerializer()
    # author = serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_absolute_url")

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "image",
            "snippet",
            "author",
            "category",
            "comment",
            "status",
            "absolute_url",
            "relative_url",
            "created_at",
            "published_at",
        ]
        read_only_fields = ["id", "created_at", "author"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        rep["category"] = CategorySerializer(
            instance.category.all(), many=True, context={"request": request}
        ).data
        rep["comment"] = CommentSerializer(
            instance.comment.all(), many=True, context={"request": request}
        ).data
        if request.parser_context.get("kwargs"):
            rep.pop("snippet", None)
            rep.pop("absolute_url", None)
            rep.pop("relative_url", None)
        else:
            rep.pop("content", None)
        return rep

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)
