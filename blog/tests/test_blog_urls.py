from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ..views import (IndexView, 
PostDetailView, 
PostCreateView, 
PostUpdateView,
PostDeleteView,
PostListView,)

# Create your tests here.
# assert True == False, "this a test"

class TestUrl(SimpleTestCase):

    def test_url_index_resolve(self):
        url = reverse("blog:index")
        self.assertEqual(resolve(url).func.view_class, IndexView)
    
    def test_url_post_detail_resolve(self):
        url = reverse("blog:post-detail-page", kwargs={"pk": 5})
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_url_post_create_resolve(self):
        url = reverse("blog:post-create-form")
        self.assertEqual(resolve(url).func.view_class, PostCreateView)

    def test_url_post_update_resolve(self):
        url = reverse("blog:post-update-page", kwargs={"pk": 5})
        self.assertEqual(resolve(url).func.view_class, PostUpdateView)

    def test_url_post_delete_resolve(self):
        url = reverse("blog:post-delete-page", kwargs={"pk": 5})
        self.assertEqual(resolve(url).func.view_class, PostDeleteView)

    def test_url_post_list_resolve(self):
        url = reverse("blog:post-list")
        self.assertEqual(resolve(url).func.view_class, PostListView)