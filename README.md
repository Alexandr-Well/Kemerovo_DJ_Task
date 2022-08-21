# Тестовое задание

## основная ветка main в ней актуальный код, ветка database только для демонстрации mysql и docker

## Установка и запуск

1. Склонировать репозиторий с Github:

```
git clone https://github.com/Alexandr-Well/Kemerovo_DJ_Task.git
```

2. В дирректории проекта создать виртуальное окружение с учетом вашей ОС:

```
python -m venv venv
```

3. Загрузить зависимости:

```
pip install requirements.txt
```

4. Создать и применить миграции в базу данных:

```
python manage.py makemigrations
python manage.py migrate
```

5. Запустить сервер

```
python manage.py runserver
```

## Установка через Docker

1. Склонировать репозиторий с Github (ветка database):

```
git clone https://github.com/Alexandr-Well/Kemerovo_DJ_Task.git
```

2. В дирректории проекта создать виртуальное окружение с учетом вашей ОС:

```
python -m venv venv
```

3. настройка докера docker-compose build

```
docker-compose build
docker-compose up
```

4. в контейнере django 

```
python manage.py makemigrations
python manage.py migrate
```


***
## URLS
***

```
http://127.0.0.1:8000/main/ < главная добавлена пагинация 20 заметок c флагом public на страницу
(с пагинацией интерестней, чем просто с обной страницей и лимитом в sql запросе)
http://127.0.0.1:8000/main/<int:pk>/ < детальная страница заметки
http://127.0.0.1:8000/user_notice/все заметки зарегестрированного пользователя пагинация 10
http://127.0.0.1:8000/users/registration/ < регистрация нового пользователья
http://127.0.0.1:8000/users/edit_user/<int:pk>/ < изменение информации о юзере
http://127.0.0.1:8000/users/user_info/<int:pk> < просмотр профиля
http://127.0.0.1:8000/users/login/ < логин
```
