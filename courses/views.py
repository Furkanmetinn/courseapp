from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def kurslar(request):
    return HttpResponse('kurs listesi')

def details(request):
    return HttpResponse('iletisim')

def getCoursesByCategory(request,category):
    return HttpResponse(f'{category} kategorisindeki kurs listesi')


