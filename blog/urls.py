from django.urls import path
from . import views

# from django.views.generic import TemplateView, RedirectView

app_name = "blog"

urlpatterns = [
    # path('fbv/', indexView, name="fbv-test"),
    # path('AUR-redirection/', RedirectView.as_view(url="https://aur.archlinux.org/"), name="aur-redirection"),
    # path('cbv2-redirection/', RedirectView.as_view(pattern_name="blog:cbv2-test"), name="cbv2-redirection"),
    # path('redirect-view/', views.redirectView, name="redirect-view"),
    # path('cbv/', TemplateView.as_view(template_name="index.html", extra_context={"name":"koth"}), name="cbv-test"),
    # path('post-redirection/<int:pk>/', views.RedirectViewAUR.as_view(), name="post-redirection-post"),
    path('cbv2/', views.IndexView.as_view(), name="cbv2-test"),
    path('aur-redirection/', views.RedirectViewAUR.as_view(), name="aur-redirection"),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pid>/", views.PostDetailView.as_view(), name="post-detail-page"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
]