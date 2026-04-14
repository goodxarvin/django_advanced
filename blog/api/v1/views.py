from operator import truediv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import SerializerMetaclass
from .serializers import PostSerializer
from rest_framework import status
from ...models import Post
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
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

        #--------- optimized way or this wau beneath ---------
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response("not valid data")
@api_view()
def post_detail(request, pid):
    post = get_object_or_404(Post, pk=pid, status=True)
    serializer = PostSerializer(post)
    return Response(serializer.data)

    #--------- optimized way or this wau beneath ---------

    # try:
    #     post = Post.objects.get(pk=pid)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     return Response({"detail": "post does not exist"}, status=status.HTTP_404_NOT_FOUND)