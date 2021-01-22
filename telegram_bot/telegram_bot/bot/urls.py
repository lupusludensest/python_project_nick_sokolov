from django.urls import path
from .views import *


urlpatterns = [
    path('subscribers/list', SubscribersList.as_view()),
    path('messages/list/', MessagesList.as_view()),
    path('messages/add/', MessageCreate.as_view()),
    path('messages/<int:pk>/', MessageRUD.as_view()),
    path('messages/custom/list/', message_list),
    path('messages/custom/add/', message_add),
    path('messages/custom/get/<int:message_id>/', get_message),
    path('messages/custom/update/<int:message_id>/', update_message),
    path('messages/custom/delete/<int:message_id>/', delete_message),

]