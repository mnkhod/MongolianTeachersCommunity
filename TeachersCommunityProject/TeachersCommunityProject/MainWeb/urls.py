from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('news/',views.news_archive,name="news"),
    path('laws/',views.laws_archive,name="laws"),
    path('aboutUs/',views.about_us,name="aboutUs"),
    path('contactUs/',views.contact_us,name="contactUs"),
    path('news/<slug:news_id>/',views.news_single,name="newsSingle"),
    path('laws/<slug:laws_id>/',views.laws_single,name="lawsSingle"),
]
