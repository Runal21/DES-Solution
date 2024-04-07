
from django.db import models
from django.contrib.auth.models import User

class ForumPost_Create(models.Model):
    fp_title = models.CharField(max_length=200)
    fpcreate_content = models.TextField()
    fp_user = models.ForeignKey(User, on_delete=models.CASCADE)  # Changed from author to user
    fp_image = models.ImageField(upload_to='static/forum_images/', null=True, blank=True)
    fpcreate_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ForumPost_Comment(models.Model):
    forumpost = models.ForeignKey(ForumPost_Create, on_delete=models.CASCADE, related_name='comments')
    fp_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fpcomment_content = models.TextField()
    fpcomment_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'
