from django.contrib import admin
from .models import *

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'user_name',
        'telegram_id'
    ]
