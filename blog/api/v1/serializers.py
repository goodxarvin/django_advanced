from rest_framework import serializers
from ...models import Post, Category
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
        
class PostSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    # content = serializers.ReadOnlyField() or --> content = serializers.CharField(read_only=True)
    # category = CategorySerializer()
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_absolute_url")



    class Meta:
        model = Post
        fields = ['id', 'title', 'content', "snippet", "author", "category", 'status', "absolute_url", "relative_url", 'created_at' ,'published_at']
        # read_only_fields = ["id", "created_at"]
    
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        print(request.__dict__)
        rep = super().to_representation(instance)
        rep["category"] = CategorySerializer(instance.category).data
        if request.parser_context.get("kwargs"):
            rep.pop("snippet", None)
            rep.pop("absolute_url", None)
            rep.pop("relative_url", None)
        return rep