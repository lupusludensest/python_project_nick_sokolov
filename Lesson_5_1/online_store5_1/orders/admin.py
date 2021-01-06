from django.contrib import admin
from .models import *

# 1
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'date',
        'pyment_method',
        'delivery_method',
        'delivery_date',
        'total_price',
    ]


# 2
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'order',
        'product',
        'date',
        'item_price',
        'product_quantity',
        'sub_total',
    ]