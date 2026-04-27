from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .. import views

urlpatterns = [
    # registration 
    path("registration/", views.RgistrationAPIView.as_view(), name="account-register"),

    #change password

    path("change-password/", views.ChangePasswordAPIView.as_view(), name="change-password"),

    path("test/", views.SendVerificationEmailAPIView.as_view(), name="test-email"),

    #activation
    # path("activation/confirm/")

    #resend activation
    # path("activation/resend/")


    #reset password

    #token login
    path("login/token/", views.CustomAuthToken.as_view(), name="auth-token"),
    path("logout/token/", views.CustomDiscardToken.as_view(), name="discard-token"),

    #jwt login
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]