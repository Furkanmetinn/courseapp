from django.shortcuts import redirect,render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

#Key:value
data={
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web gelistirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

# Create your views here.

def kurslar(request):
    return HttpResponse('kurs listesi')

def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfasi")

def getCoursesByCategory(request,category_name):
    try:
       category_text=data[category_name];
       return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("Yanlış kategori seçimi")

def getCoursesByCategoryId(request,category_id):
    #1-2-3=>
    category_list=list(data.keys())
    if(category_id>len(category_list)):
       return HttpResponseNotFound("yanlış kategori seçimi")
    redirect_text=category_list[category_id-1]


    return redirect('/kurs/kategori/'+redirect_text)


