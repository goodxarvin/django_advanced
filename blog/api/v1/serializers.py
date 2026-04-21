from operator import truediv
from unicodedata import category
from rest_framework import serializers
from ...models import Post, Category
# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    # content = serializers.ReadOnlyField() or --> content = serializers.CharField(read_only=True)
    snippet = serializers.ReadOnlyField(source="get_snippet")

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', "snippet", "author", "category", 'status', 'created_at' ,'published_at']
        # read_only_fields = ["id", "created_at"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]