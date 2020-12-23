from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import EmailCollector

# Create your views here.
def index(request):
    return HttpResponse(f'Hello, God"s world(Lesson_4_1)!!!')

def test_json_data(request):
    resp_data = {}
    resp_data['name'] = 'Gurov Vic(Lesson_4_1)'
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
#     return HttpResponse(f'Hey, carma will get you(Lesson_4_1)!!!')

def carma(request):
    return render(request, 'carma_counter.html', {})

def add_user_data(request):
    resp_data =  {}
    if request.method == 'POST':
        try:
            request_json = json.loads(request.body)
            EmailCollector.objects.create(
                first_name = request_json['first_name'],
                last_name = request_json['last_name'],
                department_name = request_json['department_name'],
                salary = request_json['salary'],
                email = request_json['email'],
                phone_num = request_json['phone_num']
            )
            resp_data = {"message": "new record created", "status": True, "method": request.method}
        except BaseException as error:
            resp_data = {"message": str(error), "status": False, "method": request.method}
    else:
            resp_data = {"message": "unknown method", "status": False, "method": request.method}
    return JsonResponse(resp_data)
