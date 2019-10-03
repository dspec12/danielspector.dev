from django.db import models
from datetime import datetime
from autoslug import AutoSlugField


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title")
    description = models.CharField(max_length=200)
    pub_date = models.DateField(default=datetime.today())
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
