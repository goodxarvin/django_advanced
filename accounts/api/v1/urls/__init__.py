from django.urls import path, include

app_name = "api-v1"

urlpatterns = [
    path("", include("accounts.api.v1.urls.accounts"), name="account-urls"),
    path("profile/", include("accounts.api.v1.urls.profiles"), name="profile-urls")
]