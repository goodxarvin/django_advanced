import pytest
from django.utils import timezone
from datetime import datetime
from rest_framework.test import APIClient
from accounts.models import User
from ..models import Category
from django.urls import reverse


@pytest.fixture
def user_object():
    user = User.objects.create_user(
        email="test@test.test",
        password="12345678",
        is_verified=True,
    )
    return user

@pytest.fixture
def category_object():
    category = Category.objects.create(
        name="python"
    )
    return category

@pytest.mark.django_db  # allow pytest to access database
class TestPostAPI:

    client = APIClient()

    def test_get_post_response_200_status(self, user_object):
        # find post list url
        url = reverse("blog:api-v1:post-list")
        # client creation
        self.client.force_login(user=user_object)
        response = self.client.get(url)
        assert response.status_code == 200


    def test_create_post_response_401_status(self, user_object):

        # client.force_login(user=self.user)
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "pytest",
            "content": "test",
            # "author": None,
            "status": True,
            # "category": None,
            "published_at": datetime.now(),
        }
        response = self.client.post(url, data)
        assert response.status_code == 401

    def test_postMehod_post_response_201_status(self, user_object):
        category = Category.objects.create(name="python")
        data = {
            "title": "pytest",
            "content": "test",
            # "author": None,
            "status": True,
            "category": category.id,
            "published_at": timezone.now(),
        }
        self.client.force_login(
            user=user_object
        )  # or self.client.force_login(user=user_object)
        url = reverse("blog:api-v1:post-list")
        response = self.client.post(url, data)
        assert response.status_code == 201

    def test_postMehod_post_invalid_data_response_400_status(self, user_object):
        data = {
            "title": "pytest",
            "content": "test",
            # "author": None,
            # "category": None,
        }
        self.client.force_authenticate(
            user=user_object
        )  # or self.client.force_login(user=user_object)
        url = reverse("blog:api-v1:post-list")
        response = self.client.post(url, data)

        assert response.status_code == 400

    # finished tests
