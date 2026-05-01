from django.test import SimpleTestCase, TestCase
from ..forms import PostForm
from datetime import datetime
from ..models import Category

class TestPostForm(TestCase):

    def test_true_post_form_content(self):
        category_obj = Category.objects.create(name="koth")
        form = PostForm(data={
            "title": "test_title",
            "content": "test_content",
            "status": True,
            "category": category_obj,
            "published_at": datetime.now()
        })
        validate_form = form.is_valid()
        self.assertTrue(validate_form)

    def test_false_post_form_content(self):
        category_obj = Category.objects.create(name="koth")
        form = PostForm(data={})
        validate_form = form.is_valid()
        self.assertFalse(validate_form)