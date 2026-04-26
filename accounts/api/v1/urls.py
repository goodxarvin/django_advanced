from django.urls import path, include
from . import views


app_name = "api-v1"

urlpatterns = [
    path("registration/", views.RgistrationAPIView.as_view(), name="account-register"),
    path("login/token/", views.CustomAuthToken.as_view(), name="auth-token"),
    path("logout/token/", views.CustomDiscardToken.as_view(), name="discard-token"),

]