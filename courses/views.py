from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def kurslar(request):
    return HttpResponse('kurs listesi')
def programlama(request):
    return HttpResponse('programlama kurs listesi')

def mobiluygulamalar(request):
    return HttpResponse('mobil uygulamalar kurs listesi')

def details(request):
    return HttpResponse('iletisim')
