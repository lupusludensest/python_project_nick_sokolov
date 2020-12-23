from django.contrib import admin
from .models import *

@admin.register(EmailCollector) # wrapping function
class EmailCollectorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'time_create'
    ]

# admin.site.register(EmailCollector, EmailCollectorAdmin)



