
from django.db import models
from django.contrib.auth.models import User

class ForumPost_Create(models.Model):
    fpcreate_title = models.CharField(max_length=200)
    fpcreate_content = models.TextField()
    fpcreate_user = models.ForeignKey(User, on_delete=models.CASCADE)  # Changed from author to user
    fpcreate_image = models.ImageField(upload_to='static/forumpost/forum_images/', null=True, blank=True)
    fpcreate_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
