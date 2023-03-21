from django import template
from ..models import Menu

register = template.Library()


@register.inclusion_tag('django_menu/menu_tag.html')
def draw_menu(menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        menu = False
        name = menu_name

    return {'menu': menu, 'name': menu_name}