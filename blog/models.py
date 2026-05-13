from django.db import models
from django.urls import reverse

# from django.contrib.auth import get_user_model
# from accounts.models import Profile

# User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    category = models.ManyToManyField("Category")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[:5]

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comment")
    content = models.TextField(max_length=500)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies")

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.id}, {self.user}"