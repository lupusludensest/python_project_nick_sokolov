from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class User(models.Model):
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    title = models.CharField(verbose_name = 'Title', max_length=50, blank=False, null=False)
    description = models.CharField(verbose_name = 'Description', max_length=250, blank=False, null=False)
    time_create = models.DateTimeField(verbose_name = 'Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now_add=True)
    d_of_b = models.DateField(verbose_name='Data', blank=False, null=False, editable=True)

class Blog(models.Model):
    class Meta:
        db_table = 'blogs'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    title = models.CharField(verbose_name='Title', max_length=150, blank=False, null=False)
    description = models.CharField(verbose_name='Description', max_length=250, blank=False, null=False)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now_add=True)

class Post(models.Model):
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    user = models.ForeignKey(User, verbose_name='User', max_length=50, blank=False, null=False, on_delete = models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name='Blog', max_length=50, blank=False, null=False, on_delete = models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=50, blank=False, null=False)
    post_body = models.TextField(verbose_name='Post body', blank=False, null=False)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now_add=True)

class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(verbose_name='Title', max_length=150, blank=False, null=False)
    description = models.CharField(verbose_name='Description', max_length=250, blank=False, null=False)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now_add=True)
    category_img_url = models.CharField(verbose_name='Image', max_length=250, blank=True, null=True)

class Post_category(models.Model):
    class Meta:
        db_table = 'post categories'
        verbose_name = 'Post category'
        verbose_name_plural = 'Post categories'

    post = models.ForeignKey(Post, verbose_name='Post', max_length=50, blank=False, null=False, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Category', max_length=50, blank=False, null=False, on_delete = models.CASCADE)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now_add=True)

class Comment(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    # reference_comment = models.ForeignKey(Comments, verbose_name='Reference comment id', max_length=50, blank=False, null=False)
    user = models.ForeignKey(User, verbose_name='User', max_length=50, blank=False, null=False, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='Post', max_length=50, blank=False, null=False, on_delete = models.CASCADE)
    comment_txt = models.CharField(verbose_name='Comment', max_length=150, blank=False, null=False)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now_add=True)

class Tag(models.Model):
    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    title = models.CharField(verbose_name='Title', max_length=150, blank=False, null=False)
    description = models.CharField(verbose_name='Description', max_length=250, blank=False, null=False)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now_add=True)
    category_img_url = models.CharField(verbose_name='Image', max_length=250, blank=True, null=True)

class Post_tag(models.Model):
    class Meta:
        db_table = 'post tag'
        verbose_name = 'Post tag'
        verbose_name_plural = 'Post tags'

    post = models.ForeignKey(Post, verbose_name='Post', max_length=50, blank=False, null=False, on_delete = models.CASCADE)
    tag = models.ForeignKey(Tag, verbose_name='Tag', max_length=50, blank=False, null=False, on_delete = models.CASCADE)


