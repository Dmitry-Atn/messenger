from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    read = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return 'From ' + self.sender.username + ' to ' + self.recipient.username + '\n' + str(self.sent_at)


def create_message(sender, recipient, body):
    Message(sender=sender, recipient=recipient, body=body).save()
