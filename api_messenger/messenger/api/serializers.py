from rest_framework import serializers
from messenger.models import Message
from django.contrib.auth.models import User


class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ["pk", "sender", "recipient", "sent_at", "body", "read", "deleted"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


