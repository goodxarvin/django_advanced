from django.urls import path
from .. import views

urlpatterns = [
    path("", views.ProfileDetailAPIView.as_view(), name="account-profile"),
]
