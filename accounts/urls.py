from django.urls import path, include
from .views import send_mail, test

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("api/v1/", include("accounts.api.v1.urls"), name="api-accounts-v1"),
    path("api/v2/", include("djoser.urls"), name="api-accounts-v2"),
    path("api/v2/", include("djoser.urls.jwt"), name="api-accounts-v2-jwt"),
    path("send-mail/", send_mail, name="send-mail"),
    path("test/", test, name="test"),
]

