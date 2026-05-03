from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime
from django.utils import timezone
from random import choice
from accounts.models import User, Profile
from ...models import Post, Category


category_list = [
    "dev",
    "python",
    "django",
    "programming",
    "ssh",
    "harley-davidson",
]


class Command(BaseCommand):
    help = "insert dummy data"

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self.fake = Faker()

    def handle(self, *args, **options):
        for name in category_list:
            Category.objects.get_or_create(name=name)


        for _ in range(5):
            user = User.objects.create_user(email=self.fake.email(), password="test@123456")
            profile = Profile.objects.get(user=user)
            profile.first_name = self.fake.first_name()
            profile.last_name = self.fake.last_name()
            profile.phone = self.fake.phone_number()
            profile.country = self.fake.country()
            profile.save()
            for _ in range(10):
                post = Post.objects.create(
                    title = self.fake.paragraph(nb_sentences=1),
                    content = self.fake.paragraph(nb_sentences=10),
                    author = profile,
                    # category = Category.objects.get(name=choice(category_list)),
                    status = choice([True, False]),
                    published_at = timezone.now(),
                    image = "images/sample.jpg"
                )
                for _ in range(choice([1, 2, 3])):
                    post.category.add(Category.objects.get(name=choice(category_list)))



            



