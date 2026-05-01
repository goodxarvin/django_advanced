from datetime import datetime
from django.contrib.auth.mixins import UserPassesTestMixin
from django.test import TestCase, testcases
from ..models import Post, Category
from django.contrib.auth import get_user_model
from accounts.models import User


class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email="koth_test@dd.com", password="qazwsx123890")
        self.post = Post.objects.create(
            author = self.user.profile,
            title = "test_post",
            content = "test_content",
            status = True,
            category = None,
            published_at = datetime.now(),
        )
        return super().setUp()

    def test_create_post_model(self):
        # post = self.post
        self.assertTrue(Post.objects.filter(pk=self.post.id).exists())
        self.assertEqual(self.post.title, "test_post")
