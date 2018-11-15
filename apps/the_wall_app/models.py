from django.db import models
from apps.login_and_registration.models import User

class message(models.Model):
    created_by = models.ForeignKey(User, related_name='messages_sent')
    content = models.TextField()
    sent_to = models.ForeignKey(User, related_name='messages_received')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)