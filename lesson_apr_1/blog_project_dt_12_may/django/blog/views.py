from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def my_test_view(request):
    return HttpResponse('Some text')

def my_first_page(request):
    return render(request, 'index.html', {
        'my_param': 'My text',
        'my_param2': 'My text2',
    })
