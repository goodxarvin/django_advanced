from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post

@api_view()
def post_list(request):
    return Response({"arvin": "name"})

@api_view()
def post_detail(request, pid):
    post = Post.objects.get(pk=pid)
    print(post.__dict__)
    serializer = PostSerializer(post)
    print(serializer.__dict__)
    return Response(serializer.data)