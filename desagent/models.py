# models.py

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    cm_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cm_message = models.TextField()
    cm_response = models.TextField()
    cm_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cm_user.username}: {self.cm_message}'