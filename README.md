### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Rased1983/api_final_yatube.git
```

```
cd yatube_api/
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
Создать суперюзера:

```
python manage.py createsuperuser
```
### Как пользоваться проектом:

Документация к проекту доступна по адресу: http://127.0.0.1:8000/redoc/

Для аторизации необходимо получить JWT token(см. документацию)


### Технологии:

При создании проекта использованы:
1) Django 2.2.16
2) Python 3.7.9
3) Djangorestframework 3.12.4
4) Библиотека идентификации по JWT-токенам Djoser 2.1.0
и д.р.


### Автор проекта Роман)