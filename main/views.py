from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.template.defaultfilters import first


def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1}, 
        'bool': True
    }
    
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse('About page')