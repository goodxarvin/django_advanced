from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import status
from ...models import Post
from django.shortcuts import get_object_or_404


#FBV for post list: 

"""
#@api_view(['GET', 'POST'])

# always put permissions after api_views: 

#@permission_classes([IsAuthenticated,])
#@permission_classes([IsAuthenticatedOrReadOnly,])
def post_list(request):
    if request.method == "GET":
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        #--------- optimized way or this way below ---------
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response("not valid data")"""

#CBS for post list:


class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


#FBV for post detail:

'''@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pid):
    post = get_object_or_404(Post, pk=pid, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({"detail": "post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    #--------- optimized way or this wau beneath ---------

    # try:
    #     post = Post.objects.get(pk=pid)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     return Response({"detail": "post does not exist"}, status=status.HTTP_404_NOT_FOUND)'''


#CBS for post detail:
class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self, request ,pid):
        post = get_object_or_404(Post, pk=pid, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, pid):
        post = get_object_or_404(Post, pk=pid, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pid):
        post = get_object_or_404(Post, pk=pid, status=True)
        serializer = self.serializer_class(post)
        post.delete()
        return Response({"detail": "post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


