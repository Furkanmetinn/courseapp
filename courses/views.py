from datetime import date
from django.shortcuts import redirect,render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

#Key:value
data={
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web gelistirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
}

db={
    "courses":[
        {
            "title":"javascript kursu",
            "description":"javascript kurs açıklaması",
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
            "slug":"javascript-kursu",
            "date":date(2022,10,10),
            "is-active":True
        },
         {
            "title":"python kursu",
            "description":"python kurs açıklaması",
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
            "slug":"python-kursu",
            "date":date(2022,12,10),
            "is-active":True

        },
         {
            "title":"web geliştirme kursu",
            "description":"web geliştirme kurs açıklaması",
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
            "slug":"web-gelistirme-kursu",
            "date":date(2022,9,10),
            "is-active":True

        },

    ],
    "categories":["programlama","web-geliştirme","mbil uygulamalar"]

}
# Create your views here.

def index(request):
    category_list=list(data.keys())

    return render(request,'courses/index.html',{
        'categories':category_list
    })

def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfasi")

def getCoursesByCategory(request,category_name):
    try:
       category_text=data[category_name];
       return render(request,'courses/courses.html',{
           'category':category_name,
           'category_text':category_text
       })
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


