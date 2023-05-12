from rest_framework import serializers

from .models import Conversations


class ConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversations
        fields = ("id", 'product', 'name', 'email', 'subject', 'telephone', 'message')