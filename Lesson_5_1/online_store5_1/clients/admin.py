from django.contrib import admin
from .models import *

# 1
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'address',
        'city',
        'state',
        'country',
        'postal_code'
    ]
