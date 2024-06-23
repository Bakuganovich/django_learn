from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render


menu = ['Главная','Мой профиль' ,'О нас']
data_db = [
    {'id': 1, 'name': 'Adidas ozweego','description': 'Adidas Originals Ozweego Skating Low-top Sports Shoes - это классические спортивные кроссовки, вдохновленные ретро-движением, которое было новым в стиле в 90-х годах', 'categories':'обувь', 'is_published': True},
    {'id': 2, 'name': 'Adidas yung1', 'description': 'Adidas Yung 1 - это стильные и комфортные кроссовки, которые станут отличным дополнением к вашему гардеробу.','categories': 'обувь', 'is_published': False},
    {'id': 3, 'name': 'Adidas boost', 'description': 'Уникальная пористая (ячеистая) структура помогает высвобождать энергию при каждом шаге, поскольку гранулы имеют низкую плотность. ','categories': 'обувь', 'is_published': True}
]

def main(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'products': data_db
    }
    return render(request,'main/main.html', context=data)


def about(request):
    return render(request,'main/about.html')


def main_page(request, number_page):
    if int(number_page)>100:
        return redirect('home', permanent=301)
    return HttpResponse("Cтраница с пагинацией:  " + str(number_page))


def search_clothes(request, name_clothes):
    if len(name_clothes)>50:
        return redirect('home','1')
    return HttpResponse("Вот, что мы нашли по запросу: " + str( name_clothes))


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Нихуя не понял, уточни запрос :)</h1> <p>Ошибка 404</p>")

