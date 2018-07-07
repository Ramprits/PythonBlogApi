from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    categories = models.ForeignKey(
        Category, on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
