# Тестовое задание


## Установка и запуск

1. Склонировать репозиторий с Github:
```
git clone https://github.com/Alexandr-Well/Kemerovo_DJ_Task.git
```

2. В дирректории проекта создать виртуальное окружение с учетом вашей ОС:

```
python -m venv venv
```

3. Создать и применить миграции в базу данных:
```
python manage.py makemigrations
python manage.py migrate
```
4. Запустить сервер
```
для каждой команды в отдельном терменале
python manage.py runserver

```

***
## URLS
***
```
http://127.0.0.1:8000/main/ < главная
http://127.0.0.1:8000/main/<int:pk>/ < детальная страница заметки
http://127.0.0.1:8000/users/registration/ < регистрация нового пользователья
http://127.0.0.1:8000/users/edit_user/<int:pk>/ < изменение информации о юзере
http://127.0.0.1:8000/users/user_info/ < просмотр профиля
http://127.0.0.1:8000/users/login/ < логин
```
