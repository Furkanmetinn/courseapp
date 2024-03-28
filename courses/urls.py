from django.urls import path
from . import views
#http://127.0.0.1:8000/client :>Anasayfa
#http://127.0.0.1:8000/client/kurslar :>kurs listesi


urlpatterns = [
    path('',views.index),
    path('<kurs_adi>',views.details),
    path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<str:category_name>',views.getCoursesByCategory,name='courses_by_category'),

    



]
