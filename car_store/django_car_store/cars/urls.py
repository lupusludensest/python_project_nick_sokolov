from django.urls import path
from .views import *

urlpatterns = [
    path('brands/list/', GetBrandList.as_view()),

]