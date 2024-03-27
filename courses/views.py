from django.shortcuts import redirect,render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

#Key:value
data={
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web gelistirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

# Create your views here.

def kurslar(request):
    list_items=""
    category_list=list(data.keys())

    for category in category_list:
        redirect_url=reverse('courses_by_category',args=[category])
        list_items +="<li><a href='{redirect_url}'>{category}</a></li>"

    html=f"<h1>kurs listesi</h1><ul>{list_items}</ul>"
    return HttpResponse(html)

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
    category_name=category_list[category_id-1]

    redirect_url=reverse('courses_by_category',args=[category_name])
    return redirect(redirect_url)


