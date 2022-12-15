from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.shortcuts import render
from .models import *
import random

menu = [{"title": "Главная страница", "url_name": "home"},
        {"title": "Виды Шпицев", "url_name": "types"},
        {"title": "О сайте", "url_name": "about"},
        {"title": "Войти", "url_name": "login"},
]

def handler404(request, *args, **argv):
    response = render(request, '404.html')
    response.status_code = 404
    return response

def index(request):
    spitz = Spitz.objects.all()
    types = TypesSpitz.objects.all()
    context = {
        "types": types,
        "type_selected": 0,
        "spitz": spitz,
        "menu": menu,
        "title": "Главная страница"
    }
    return render(request, "index.html", context=context)

def about(request):
    types = TypesSpitz.objects.all()
    context = {
        "types": types,
        "menu": menu,
        "title": "О сайте"
    }
    return render(request, "about.html", context=context)

def types(request):
    types = TypesSpitz.objects.all()
    context = {
        "types": types,
        "menu": menu,
        "title": "Виды Шпицев"
    }
    return render(request, "types.html", context=context)

def login(request):
    return HttpResponse("Авторизация")

def show_type(request, type_id):
    spitz_type = TypesSpitz.objects.filter(pk=type_id)
    spitz_type = spitz_type[0]
    types = TypesSpitz.objects.all()
    context = {
        "types": types,
        "menu": menu,
        "title": spitz_type.title,
        "spitz_type": spitz_type
    }
    return render(request, "spitztype.html", context=context)
