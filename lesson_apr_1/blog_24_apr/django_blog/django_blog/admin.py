from django.contrib import admin
from django_blog.models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['time_create']

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['time_create']
admin.site.register(Post, PostAdmin)


