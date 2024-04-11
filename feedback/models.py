from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feedback(models.Model):
    fb_uname = models.CharField(max_length=20)
    fb_email = models.EmailField()
    fb_content = models.TextField()
    fb_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.fb_uname}"

class FeedbackReply(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    fbr_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    fbr_reply_content = models.TextField()
    fbr_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply to feedback: {self.feedback.id} by {self.fbr_admin} to {self.feedback.fb_uname}"
    
