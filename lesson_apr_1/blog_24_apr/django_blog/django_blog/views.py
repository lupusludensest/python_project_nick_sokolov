from django.shortcuts import render
from django.http.response import HttpResponse
from django_blog.models import Post

# Create your views here.

def my_test_view(request):
    return HttpResponse('Some text')

def my_first_page(request):
    return render(request, 'index.html', {
        'my_param': 'My text',
        'my_param2': 'My text2',
    })

def main_feed(request):

    posts = Post.objects.all()

    return render(request, 'feed.html', {
        'posts_list': posts
    })


def get_post(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'page.html', {
        'post': post
    })
