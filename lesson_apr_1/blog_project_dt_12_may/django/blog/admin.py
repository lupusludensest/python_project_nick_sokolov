from django.contrib import admin
from blog.models import Category, Post, Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['time_create']

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['time_create']

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'reference_comment', 'comment_txt', 'post', 'time_create']
    list_filter = ['time_create']

admin.site.register(Comment, CommentAdmin)
