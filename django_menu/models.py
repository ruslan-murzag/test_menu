from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    url = models.CharField(max_length=255, blank=True, verbose_name='ссылка')
    parent = models.ForeignKey('self', verbose_name='родитель',  null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    items = models.ManyToManyField(MenuItem)

    def __str__(self):
        return self.name

