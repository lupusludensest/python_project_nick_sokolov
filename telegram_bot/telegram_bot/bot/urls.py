from django.urls import path
from .views import SubscribersList, MessagesList, MessageCreate, MessageRUD, message_list


urlpatterns = [
    path('subscribers/list', SubscribersList.as_view()),
    path('messages/list/', MessagesList.as_view()),
    path('messages/add/', MessageCreate.as_view()),
    path('messages/<int:pk>/', MessageRUD.as_view()),
    path('messages/custom_list/', message_list)
]