from django.db import models
class Article(models.Model):
    art_author = models.CharField(max_length=50)
    art_title = models.CharField(max_length=100)
    art_content = models.TextField()
    art_image = models.ImageField(upload_to='static/article/article_images')
    art_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.art_title
