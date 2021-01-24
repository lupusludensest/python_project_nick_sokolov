from django.urls import path
# from .views import SubscribersList, MessagesList, MessageCreate, MessageRUD, message_list, message_add, get_message, update_message, delete_message
from .views import *


urlpatterns = [
    path('subscribers/list', SubscribersList.as_view()), # 1 class SubscribersList
    path('messages/list/', MessagesList.as_view()), #2 class MessagesList
    path('messages/add/', MessageCreate.as_view()), #3 class MessageCreate
    path('messages/<int:pk>/', MessageRUD.as_view()), #4 class MessageRUD
    path('messages/custom/list/', message_list), # 5 GET
    path('messages/custom/add/', message_add), # 6 POST
    path('messages/custom/get/<int:message_id>/', get_message), # 7 GET
    path('messages/custom/update/<int:message_id>/', update_message), # 8 PUT/PATCH
    path('messages/custom/delete/<int:message_id>/', delete_message), # 9 DELETE

]