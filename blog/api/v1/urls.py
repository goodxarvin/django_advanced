from codecs import lookup
from warnings import simplefilter
from rest_framework_nested import routers
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter

router = routers.DefaultRouter()
router.register("post", views.PostViewSet, basename="post")
router.register("category", views.CategoryViewSet, basename="category")

post_router = routers.NestedDefaultRouter(router, "post", lookup="post")
post_router.register("comments", views.CommentViewSet, basename="post-comments")

# from django.views.generic import TemplateView, RedirectView

app_name = "api-v1"

# urlpatterns = [
#     # CBS: path("post/", views.PostList.as_view(), name="post-list"),
#     # FBS: path("post/", views.post_list, name="post-list"),
#     # CBS: path("post/<int:pk>", views.PostDetail.as_view(), name="post-detail"),
#     # FBS: path("post/<int:pid>", views.post_detail, name="post-detail"),
#     path("post/", views.PostViewSet.as_view({"get": "list", "post": "create"}), name="post-viewset-list"),
#     path("post/<int:pk>/", views.PostViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="post-viewset-detail")
# ]

urlpatterns = router.urls + post_router.urls
