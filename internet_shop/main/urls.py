from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('about/', about, name='about_us'),
    path('<int:number_page>', main_page, name='home_page'),
    path('clothes/<slug:name_clothes>/', search_clothes, name='name_clothes'),
]
