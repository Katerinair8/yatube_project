from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):    
    return HttpResponse('Главная страница')


def group_posts(requests, slug):
    return HttpResponse ('Cтраница с постами, отфильтрованными по группам')
    