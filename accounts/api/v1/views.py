from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.response import Response
import jwt
from mail_templated import EmailMessage
from decouple import config
from .utils import EmailThread
from .serializers import (
    RegistrationSerializer,
    CustomAuthTokenSerializer,
    CustomTokenObtainPairSerializer,
    ChangePasswordSerializer,
    ProfileDetailSerializer,
)
from ...models import Profile

# from django.core.mail import send_mail


User = get_user_model()


# registration view
class RgistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def get_token_for_user(self, user) -> dict[str, str]:
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data["email"]
            user_object = get_object_or_404(User, email=email)
            access_token = self.get_token_for_user(user_object)
            email_object = EmailMessage(
                subject="Verification Email",
                template_name="email/verification.tpl",
                context={
                    "access_token": access_token,
                    "name": email,
                    "id": user_object.id,
                },
                from_email="from@example.com",
                to=["to@example.com"],
            )

            email_thread = EmailThread(email_object).start()

            data = {
                "email": serializer.validated_data["email"],
                "id": user_object.id,
                "details": "email sent and registration successful",
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# normal token creation view
class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "user_id": user.pk, "email": user.email})


# dicard normal token view
class CustomDiscardToken(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            {"detail": "logged out successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordAPIView(generics.GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["wrong password"]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"details": "password changed successfully"},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = ProfileDetailSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


# class SendVerificationEmailAPIView(generics.GenericAPIView):

#     def get_token_for_user(self, user) -> dict[str, str]:
#         refresh = RefreshToken.for_user(user)
#         return str(refresh.access_token)


#     def get(self, request, *args, **kwargs):
#         self.email = self.request.user.email
#         user_object = get_object_or_404(User, email=self.email)
#         access_token = self.get_token_for_user(user_object)
#         email_object = EmailMessage(
#             subject="Verification Email",
#             template_name="email/verification.tpl",
#             context={"access_token": access_token, "name": "John Doe", "cid_photo": "my_photo"},
#             from_email="from@example.com",
#             to=["to@example.com"]
#         )

#         email_thread = EmailThread(email_object).start()
#         return Response({"details": "email sent"})
# email.send()
# send_mail("email/verification.tpl", {"name": "John Doe"}, "from@example.com", ["to@example.com"] )


class ResendVrificationsAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get_token_for_user(self, user) -> dict[str, str]:
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def post(self, request, *args, **kwargs):
        self.email = request.user.email
        user_object = get_object_or_404(User, email=self.email)
        if not user_object.is_verified:
            access_token = self.get_token_for_user(user_object)
            email_object = EmailMessage(
                subject="Verification Email",
                template_name="email/verification.tpl",
                context={
                    "access_token": access_token,
                    "name": "John Doe",
                    "cid_photo": "my_photo",
                },
                from_email="from@example.com",
                to=["to@example.com"],
            )

            email_thread = EmailThread(email_object).start()

            return Response({"details": "verification email resent successfully"})
        else:
            return Response(
                {"details": "your account has already been verified"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class VerificationAPIView(APIView):

    def get(self, request, token, *args, **kwargs):
        try:
            token_data = jwt.decode(token, config("SECRET_KEY"), algorithms=["HS256"])
            user_id = token_data["user_id"]
            # print("token: ",token_data)

        except jwt.DecodeError:
            return Response(
                {"details": "invalid jwt"}, status=status.HTTP_400_BAD_REQUEST
            )

        except jwt.ExpiredSignatureError:
            return Response(
                {"details": "expired signature"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        specified_user = User.objects.get(pk=user_id)
        if specified_user.is_verified:
            return Response({"details": "user already have been verified"})
        specified_user.is_verified = True
        specified_user.save()
        return Response({"details": "user verified successfully"})
