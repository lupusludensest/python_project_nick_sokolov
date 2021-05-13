from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Blog(models.Model):
    class Meta:
        db_table = 'blogs'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    title = models.CharField(verbose_name='Title', max_length=150, blank=False, null=False)
    description = models.CharField(verbose_name='Description', max_length=250, blank=False, null=False)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now=True)
    def __str__(self):
        return self.title

class Post(models.Model):
    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    user = models.ForeignKey(User, verbose_name='User', max_length=70, blank=False, null=False, on_delete = models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name='Blog', max_length=70, blank=False, null=False, on_delete = models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=70, blank=False, null=False)
    post_body = models.TextField(verbose_name='Post body', blank=False, null=False)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(verbose_name='Title', max_length=250, blank=False, null=False)
    description = models.CharField(verbose_name='Description', max_length=250, blank=False, null=False)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now=True)
    category_img_url = models.CharField(verbose_name='Image', max_length=250, blank=True, null=True)
    def __str__(self):
        return self.title

class PostCategory(models.Model):
    class Meta:
        db_table = 'post categories'
        verbose_name = 'Post category'
        verbose_name_plural = 'Post categories'

    post = models.ForeignKey(Post, verbose_name='Post', max_length=70, blank=False, null=False, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Category', max_length=70, blank=False, null=False, on_delete = models.CASCADE)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now=True)
    def __str__(self):
        return self.category

class Comment(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    reference_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Reference comment id', max_length=70)
    user = models.ForeignKey(User, verbose_name='User', max_length=70, blank=False, null=False, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='Post', max_length=70, blank=False, null=False, on_delete = models.CASCADE)
    comment_txt = models.CharField(verbose_name='Comment', max_length=150, blank=False, null=False)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now=True)
    def __str__(self):
        return self.comment_txt

class Tag(models.Model):
    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    title = models.CharField(verbose_name='Title', max_length=150, blank=False, null=False)
    description = models.CharField(verbose_name='Description', max_length=250, blank=False, null=False)
    time_create = models.DateTimeField(verbose_name='Creation time', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Update time', auto_now=True)
    category_img_url = models.CharField(verbose_name='Image', max_length=250, blank=True, null=True)
    def __str__(self):
        return self.title

class PostTag(models.Model):
    class Meta:
        db_table = 'post tag'
        verbose_name = 'Post tag'
        verbose_name_plural = 'Post tags'

    post = models.ForeignKey(Post, verbose_name='Post', max_length=70, blank=False, null=False, on_delete = models.CASCADE)
    tag = models.ForeignKey(Tag, verbose_name='Tag', max_length=70, blank=False, null=False, on_delete = models.CASCADE)
    def __str__(self):
        return f'Tag for {self.post}: {self.tag}'