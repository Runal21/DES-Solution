from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    art_author = models.CharField(max_length=50)
    art_title = models.CharField(max_length=100)
    art_content = models.TextField()
    art_image = models.ImageField(upload_to='static/article_images', default='article_images/default.jpg')
    art_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
