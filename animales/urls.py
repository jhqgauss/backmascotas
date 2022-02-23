from django.urls import path,include,re_path
from animales import views



urlpatterns= [
    re_path(r'^animal/$',views.animalApi),
    re_path(r'^animal/([0-9]+)$',views.animalApi),  
]
     
