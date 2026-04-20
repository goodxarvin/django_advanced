from email.mime import base
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("post", views.PostViewSet, basename="post")

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

urlpatterns = router.urls