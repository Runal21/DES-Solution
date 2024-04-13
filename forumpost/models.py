
from django.db import models
from django.contrib.auth.models import User

class ForumPost(models.Model):
    fp_title = models.CharField(max_length=200)
    fp_content = models.TextField()
    fp_author = models.ForeignKey(User, on_delete=models.CASCADE)
    fp_created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    cmfp_author = models.ForeignKey(User, on_delete=models.CASCADE)
    cmfp_content = models.TextField()
    cmfp_created_at = models.DateTimeField(auto_now_add=True)
