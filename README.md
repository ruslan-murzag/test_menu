Я создал проект под названием djangoproject и создал приложение django_menu
Создал 2 модели `MenuItem` и `Menu`. `MenuItem` это элементы списка `menu`. `MenuItem` имеет 3 поля `name, url, parent`. `Menu` имеет 2 поля `name, items`
<p>
Я немного не понял насчет вложенности. Но сделал следующим образом. У меня есть модель `MenuItem` в котором элементы связанны между с собой отношениями в виде (parent and child). И еще к ниму создал модель Menu Для группировки MenuItem. На сайте отображается первый уровень вложенности То есть:
`Menu > ItemMenu1 > ItemMenu1_element1`. Так же прежде чем создать элемент в Menu вам надо создать элемент в MenuItem.
<p>
Для запуска вам нужны следущие команды:
  
Установка зависимостей из requirements.txt:

`pip install -r requirements.txt`

Выполнить миграции:

`python manage.py makemigrations`

`python manage.py migrate`

Для доступа к панели администратора создайте администратора:

`python manage.py createsuperuser`

Запустите приложение:

`python manage.py runserver`

После создайте элементы в модели `MenuItem`. Создайте несколько элементов данной модели с связью `parent and child`. Для того чтобы увидить функционал.
Для фронтенда использовал Bootstrap чтобы создать меню с элементами
И после этого можете создать элементы в `Menu`.
