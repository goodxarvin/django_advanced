from django.forms import SearchInput
from django.utils.dateparse import iso8601_duration_re
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.fields import DjangoFilePathField
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, GenericAPIView
from rest_framework import mixins
from .serializers import PostSerializer, CategorySerializer
from rest_framework import status
from ...models import Post, Category
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .peginations import LargeResultSetPagination

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

#CBS for post list v1:


'''class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    # you can get the query here also: postl = Post.objects.filter(status=True)

    def get(self, request):
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''


#CBS for post list v2:

'''class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)'''


#CBS for post list v3:

class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)



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


#CBS for post detail v1:
'''
class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self, request ,pid):
        """observe the post"""
        post = get_object_or_404(Post, pk=pid, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, pid):
        """edit a post"""

        post = get_object_or_404(Post, pk=pid, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pid):
        """delete a post"""

        post = get_object_or_404(Post, pk=pid, status=True)
        post.delete()
        return Response({"detail": "post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
'''
#CBS for post detail v2:
'''
class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    # lookup_field = "id"     --> if you set the post id in urls 'id' you should use this field

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

    def patch(self, request, *args, **kwargs):
        """edit a post partially"""
        return self.update(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        """edit a post"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """delete a post"""
        return self.destroy(request, *args, **kwargs)
'''

#CBS for post detail v3:


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)



# viewset: 

'''
class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, status=True, pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        post = get_object_or_404(self.queryset, status=True, pk=pk)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        post = get_object_or_404(self.queryset, status=True, pk=pk)
        post.delete()
        return Response({"detail": "post deleted successfully"})

'''
        
# model viewset:

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["author", "category", "status"]
    search_fields = ["title", "content",]
    ordering_fields = ["created_at", "published_at"]
    pagination_class = LargeResultSetPagination

    @action(methods=["get"], detail=False)
    def get_ok(self, request):
        return Response({"result": "good ok"})

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()