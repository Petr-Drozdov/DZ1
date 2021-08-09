from django.http import Http404
from django.shortcuts import render, HttpResponse
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

ITEMS = (
    {'id': 1, 'name': 'Некий товар номер 1'},
    {'id': 2, 'name': 'Некий товар номер 2!!!'},
    {'id': 3, 'name': 'Некий товар номер 3'},
    {'id': 4, 'name': 'Некий товар номер 4'},
    {'id': 5, 'name': 'Некий товар номер 5'},
)


# Create your views here.
def index(request):
    name = 'Petr'
    return HttpResponse(f'<h1>"Изучаем django"</h1><br><b>Автор</b>: <i>{name}</i>')

def about(request):
    name = 'Petr'
    second_name = 'Dr'
    surname = 'D'
    tel = '9-999-999-99-99'
    email = '_____gmail.com'
    return HttpResponse(f'Имя: <b>{name}</b><br>Отчество: <b>{second_name}</b><br>'
                        f'Фамилия: <b>{surname}</b><br>Телефон: <b>{tel}</b><br>'
                        f'e-mail: <b>{email}<b>')


def items(request):
    items_str = "<ul>"
    # <ul>
    #     <li>Товар-1</li>
    #     <li>Товар-2</li>
    #     <li>Товар-3</li>
    # </ul>
    for item in ITEMS:
        items_str += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    items_str += "</ul>"
    return HttpResponse(items_str)


def item_details(request, id):
    for item in ITEMS:
        if item['id'] == id:
            return HttpResponse(f"""{item['name']}<br>""")
    raise Http404
