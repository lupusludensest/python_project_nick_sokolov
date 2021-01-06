from django.contrib import admin
from .models import *

# 1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_name',
        'product_brand',
        'year_of_manufacture',
        'color',
        'description',
        'price'
    ]

# 2
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'description'
    ]

# 3
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'category'
    ]