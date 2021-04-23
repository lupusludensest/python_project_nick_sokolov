from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(verbose_name='Title', max_length=200, blank=False, null=False)


class Post(models.Model):
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    user = models.ForeignKey(User, verbose_name='Owner', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=200, blank=False, null=False)
    content = models.TextField(verbose_name='Content', blank=False, null=False)
    time_created = models.DateTimeField(verbose_name='Created time', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, blank=True, null=True)
