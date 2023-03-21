1. Я создал проект под названием djangoproject и создал приложение django_menu
2. Создал 2 модели `MenuItem` и `Menu`
  a) `MenuItem` это элементы списка `menu`. И имеет 3 поля `name, url, parent`
<p>
Я немного не понял насчет вложенности. Но сделал следующим образом. У меня есть модель `MenuItem` в котором элементы связанны между с собой отношениями в виде (parent and child). И еще к ниму создал модель Menu Для группировки MenuItem. На сайте отображается первый уровень вложенности То есть:
`Menu > ItemMenu1 > ItemMenu1_element1`. Так же прежде чем создать элемент в Menu вам надо создать элемент в MenuItem.
<p>
Для запуска вам нужны следущие команды:
  
Установка зависимостей из requirements.txt:

pip install -r requirements.txt

Выполнить миграции:

python manage.py makemigrations

python manage.py migrate

Для доступа к панели администратора создайте администратора:

python manage.py createsuperuser

Запустите приложение:

python manage.py runserver

После создайте элементы в модели MenuItem
И после этого можете создать элементы в Menu
