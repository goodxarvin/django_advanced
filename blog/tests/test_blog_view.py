from django.test import TestCase, Client
from datetime import datetime
from ..models import Post
from accounts.models import User
from django.urls import reverse


class TestPostView(TestCase):

    def setUp(self) -> None:
        client = Client()
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


    def test_index_view_success(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.content).find("index"))
        self.assertTemplateUsed(response , template_name="blog/index.html")

    def test_is_user_authenticated(self):
        self.client.force_login(self.user)
        url = reverse("blog:post-detail-page", kwargs={"pk": self.post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_is_user_annonymouse(self):
        url = reverse("blog:post-detail-page", kwargs={"pk": self.post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)