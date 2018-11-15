from django.db import models
from apps.login_and_registration.models import User

class Message(models.Model):
    created_by = models.ForeignKey(User, related_name='messages_sent')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    created_by = models.ForeignKey(User, related_name='comments_sent')
    posted_on = models.ForeignKey(Message, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
