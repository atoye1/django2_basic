from django.db import models
from django.conf import settings



class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=False)
    def __str__(self):
        return f'이름: {self.name}'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_url = models.URLField(blank=True)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(allow_unicode=True, db_index= True)
    desc = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    # models.ManyToManyField()
    is_publish = models.BooleanField()

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
