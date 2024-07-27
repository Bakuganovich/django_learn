from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

gg = []

menu = [
    {'title':'Главная', 'url_name': 'home'},
    {'title':'Добавить товар', 'url_name': 'add'},
    {'title': 'Обратная связь', 'url_name': 'about_us'},
    {'title':'Войти', 'url_name': 'sing'}
]

data_db = [
    {'id': 1, 'name': 'Adidas ozweego','description': 'Adidas Originals Ozweego Skating Low-top Sports Shoes - это классические спортивные кроссовки, вдохновленные ретро-движением, которое было новым в стиле в 90-х годах', 'categories':'обувь', 'is_published': True},
    {'id': 2, 'name': 'Adidas yung1', 'description': 'Adidas Yung 1 - это стильные и комфортные кроссовки, которые станут отличным дополнением к вашему гардеробу.','categories': 'обувь', 'is_published': True},
    {'id': 3, 'name': 'Adidas boost', 'description': 'Уникальная пористая (ячеистая) структура помогает высвобождать энергию при каждом шаге, поскольку гранулы имеют низкую плотность. ','categories': 'обувь', 'is_published': True}
]

cats_db = [
    {'id': 1, 'name': 'Магазины'},
    {'id': 2, 'name': 'Акции'},
    {'id': 3, 'name': 'Поиск'}
]

def main(request):
    return render(request,'main/main.html', context={'title': 'Главная страница',
                                                                  'menu':menu,
                                                                  'products': data_db})

def add_product(request):
    return HttpResponse('Добавить товар')


def about(request):
    return render(request,'main/about.html', context={'title':'О нас', 'menu': menu})


def sing_in(request):
    return HttpResponse('Вход')


def show_post(request, post_id):
    return HttpResponse('ID' + str(post_id))

def show_categories(request, cat_id):
    return HttpResponse('id ' + str(cat_id))

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Нихуя не понял, уточни запрос :)</h1> <p>Ошибка 404</p>")

