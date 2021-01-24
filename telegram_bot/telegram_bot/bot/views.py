from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from rest_framework import generics
from .models import Subscriber, Message
from .serializers import SubscriberListSerializer, MessageListSerializer
import json
import datetime

# 1 class SubscribersList
class SubscribersList(generics.ListAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberListSerializer

#2 class MessagesList
class MessagesList(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer

#3 class MessageCreate
class MessageCreate(generics.CreateAPIView):
    serializer_class = MessageListSerializer

#4 class MessageRUD
class MessageRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer

# 5 GET
def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        data = list(messages.values('id', 'message_text'))
    else:
        data = {'status': False, 'error': 'Method is not supported'}
    return JsonResponse(data, safe=False)

# 6 POST
def message_add(request):
    status_code = 0
    json_response = {}
    json_response['status'] = False
    json_response['error_message'] = ''
    if request.method == 'POST':
        try:
            request_json = json.loads(request.body)
            new_message = Message.objects.create(
                is_sent=request_json['sent'],
                message_text = request_json['text_message']
            )
            json_response['status'] = True
            status_code = 201
            json_response['result'] = {
                'message_id': new_message.id,
                'text_message': new_message.message_text,
                'is_sent': new_message.is_sent
            }
        except BaseException:
            json_response['error_message'] = 'Bad_request'
            status_code = 400
    else:
        json_response['error_message'] = 'Method not allowed'
        status_code = 405
    return JsonResponse(json_response, status=status_code, safe=True)


# 7 GET
def get_message(request, message_id):
    status_code = 0
    json_response = {}
    json_response['status'] = False
    json_response['error_message'] = ''
    if request.method == 'GET':
        try:
            message = Message.objects.get(id=message_id)
            json_response['result'] = {
                'message_id': message.id,
                'text_message': message.message_text,
                'is_sent': message.is_sent
            }
            json_response['status'] = True
            status_code = 200
        except BaseException:
            json_response['error_message'] = 'Bad_request'
            status_code = 400
    else:
        json_response['error_message'] = 'Method not allowed'
        status_code = 405
    return JsonResponse(json_response, status=status_code, safe=True)


# 8 PUT/PATCH
def update_message(request, message_id): # message_id - point of entering
    status_code = 0 # defined variable
    json_response = {} # created the dictionary
    json_response['status'] = False # defined the key in the dictionary
    json_response['error_message'] = '' # defined the key in the dictionary
    if request.method in ['PUT', 'PATCH']: # created condition
        try: # if requested method is true/correct, 'PUT', 'PATCH'
            request_json = json.loads(request.body) # getting the text of the request as a dictionary
            message = Message.objects.get(id=message_id) # getting from the database the only one writting. # all - returns all messages; filter - returns messages by criterias
            message.message_text = request_json['message_text'] # correlates with the models
            message.is_sent = request_json['is_sent'] # correlates with the models
            message.save() # saving all above
            json_response['result'] = { # creating the sub-dictionary in the key ['result']
                'message_id': message.id,
                'text_message': message.message_text,
                'is_sent': message.is_sent
            }
            json_response['status'] = True # changing to True above json_response['status'] = False
            status_code = 200
        except BaseException: # if code is not true/correct
            json_response['error_message'] = 'Bad Request'
            status_code = 400
    else: # if method is not 'PUT', 'PATCH'
        json_response['error_message'] = 'Method Not Allowed'
        status_code = 405
    return JsonResponse(json_response, status=status_code, safe=True)


# 9 DELETE
def delete_message(request, message_id):
    status_code = 0
    json_response = {}
    json_response['status'] = False
    json_response['error_message'] = ''
    if request.method == 'DELETE':
        try:
            message = Message.objects.get(id=message_id)
            message.delete()
            json_response['status'] = True
            status_code = 200
        except BaseException:
            json_response['error_message'] = 'Bad Request'
            status_code = 400
    else:
        json_response['error_message'] = 'Method Not Allowed'
        status_code = 405
    return JsonResponse(json_response, status=status_code, safe=True)