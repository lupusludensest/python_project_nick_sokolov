from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, God's world(Lesson_4)!!!")

def test_json_data(request):
    resp_data = {}
    resp_data['name'] = 'Gurov Vic(Lesson_4)'
    book = []
    book.append({"name": "Vasya", "phone": "+1(234)444-12-31"})
    book.append({"name": "Petya", "phone": "+1(234)444-12-32"})
    book.append({"name": "Kolya", "phone": "+1(234)444-12-33"})
    book.append({"name": "Anya", "phone": "+1(234)444-12-34"})
    book.append({"name": "Janet", "phone": "+1(234)444-12-35"})
    book.append({"name": "Joahn", "phone": "+1(234)444-12-36"})
    resp_data['book'] = book
    return JsonResponse(resp_data)

# def carma(request):
#     return HttpResponse(f'Hey, carma will get you(Lesson_4)!!!')

def carma(request):
    return render(request, 'carma_counter.html', {})


