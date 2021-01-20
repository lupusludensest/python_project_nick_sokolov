from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import generics
from .models import Subscriber, Message
from .serializers import SubscriberListSerializer, MessageListSerializer


class SubscribersList(generics.ListAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberListSerializer


class MessagesList(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer


class MessageCreate(generics.CreateAPIView):
    serializer_class = MessageListSerializer


class MessageRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer

def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        data = list(messages.values('id', 'message_text'))
    else:
        data = {'status': False, 'error': 'Method is not supported'}
    return JsonResponse(data, safe=False)