from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return render(request, 'main.html')
    # return HttpResponse("Hello World")


def hello_template(request):
    name = 'Mat 22'
    age = 15
    context = {
        'name': name,
        'students': ['Baktilek', 'Dinara','Farida','Madina','Dinara','Baiel','Akylai'],
        'age' : age > 18
        }
    return render(request, 'index.html',context)
