from django.urls import path
from .views import *

urlpatterns = [
    path('test/', index),
    path('json/', test_json_data),
    path('carma/', carma),
    path('add/', add_user_data)
]