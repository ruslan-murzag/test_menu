from django.shortcuts import render
from .models import MenuItem, Menu


def menu(request):
    Menu_list = Menu.objects.all()
    current_path = request.path
    return render(request, 'django_menu/menu_page.html')


def menu_item(request, id):
    item = MenuItem.objects.get(id = id)
    return render(request, 'django_menu/menu_item.html', {'item': item})
