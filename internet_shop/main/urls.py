from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('add_product/', add_product, name='add'),
    path('about/', about, name='about_us'),
    path('sing_in/', sing_in, name='sing'),
    path('post/<int:post_id>/', show_post, name='about_product'),
    path('category/<int:cat_id>/', show_categories, name='category'),

]


