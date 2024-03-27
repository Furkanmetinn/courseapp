from django.urls import path
from . import views
#http://127.0.0.1:8000/client :>Anasayfa
#http://127.0.0.1:8000/client/kurslar :>kurs listesi


urlpatterns = [
    path('',views.kurslar),
    path('list',views.kurslar),
    path('details',views.details),
    path('<category>',views.getCoursesByCategory),
    



]
