from django.db import models

class Comment(models.Model):
    user = models.OneToOneField("accounts.Profile", on_delete=models.CASCADE)
    post = models.ForeignKey("blog.Post", on_delete=models.CASCADE, related_name="comment")
    context = models.CharField(max_length=500)


    def __str__(self):
        return f"{self.id}, {self.user}"


class Reply(models.Model):
    user = models.OneToOneField("accounts.Profile", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="reply")
    context = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.id}, {self.user}"