from django.contrib import admin
from .models import *

@admin.register(EmailCollector) # wrapping function
class EmailCollectorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'department_name',
        'salary',
        'email',
        'time_create',
        'phone_num'
    ]

# admin.site.register(EmailCollector, EmailCollectorAdmin)



