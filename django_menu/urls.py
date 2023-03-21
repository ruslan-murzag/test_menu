from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.menu, name='main_menu'),
    path('<int:id>', views.menu_item, name='menu_item')
]
