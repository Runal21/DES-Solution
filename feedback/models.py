from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    fb_uname = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    fb_email = models.EmailField(User.email)
    fb_content = models.TextField()
    fb_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.fb_uname.username}"

class FeedbackReply(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    fb_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply to feedback: {self.feedback.id} by {self.admin.username}"
