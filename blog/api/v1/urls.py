from django.urls import path, include
from . import views

# from django.views.generic import TemplateView, RedirectView

app_name = "api-v1"

urlpatterns = [
    path("post/", views.post_list, name="post-list"),
    path("post/<int:pid>", views.post_detail, name="post-detail"),

]