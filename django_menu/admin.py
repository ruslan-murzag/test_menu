from django.contrib import admin
from .models import MenuItem, Menu


@admin.register(MenuItem)
class AdminMeniItem(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')


@admin.register(Menu)
class AdminMeniItem(admin.ModelAdmin):
    list_display = ('name',)
