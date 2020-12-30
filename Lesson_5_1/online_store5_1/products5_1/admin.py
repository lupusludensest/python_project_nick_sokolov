from django.contrib import admin
from .models import *

@admin.register(Product) # wrapping function
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_name',
        'product_brand',
        'year_of_manufacture',
        'color',
        'description',
        'price'
    ]

# admin.site.register(EmailCollector, EmailCollectorAdmin)