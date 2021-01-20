from rest_framework import serializers
from .models import Subscriber, Message


class SubscriberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        # fields = ['id',
        #           'message_text'
        #           ]