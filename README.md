# Проект YaMDb

Проект YaMDb собирает отзывы пользователей на различные произведения такие как
фильмы, книги и музыка.

## Описание проекта:

API YaMDb позволяет работать со следующими сущностями:

* JWT-токен (Auth): отправить confirmation_code на переданный email, получить
  JWT-токен
  в обмен на email и confirmation_code;
* Пользователи (Users): получить список всех пользователей, создать
  пользователя,
  получить пользователя по username, изменить данные пользователя по username,
  удалить
  пользователя по username, получить данные своей учётной записи, изменить
  данные своей учётной записи;
* Произведения (Titles), к которым пишут отзывы: получить список всех объектов,
  создать
  произведение для отзывов, информация об объекте, обновить информацию об
  объекте, удалить произведение.
  пользователя по username, получить данные своей учётной записи, изменить
  данные своей учётной записи;
* Категории (Categories) произведений: получить список всех категорий, создать
  категорию, удалить категорию;
* Жанры (Genres): получить список всех жанров, создать жанр, удалить жанр;
* Отзывы (Review): получить список всех отзывов, создать новый отзыв, получить
  отзыв по id,
  частично обновить отзыв по id, удалить отзыв по id;
* Комментарии (Comments) к отзывам: получить список всех комментариев к отзыву
  по id, создать
  новый комментарий для отзыва, получить комментарий для отзыва по id, частично
  обновить комментарий к отзыву по id, удалить комментарий к отзыву по id.

## Стек технологий:

* [Python 3.7+](https://www.python.org/downloads/)
* [Django 2.2.16](https://www.djangoproject.com/download/)
* [Django Rest Framework 3.12.4](https://pypi.org/project/djangorestframework/#files)
* [Pytest 6.2.4](https://pypi.org/project/pytest/)
* [Simple-JWT 1.7.2](https://pypi.org/project/djangorestframework-simplejwt/)
* [pytest 6.2.4](https://pypi.org/project/pytest/)
* [pytest-pythonpath 0.7.3](https://pypi.org/project/pytest-pythonpath/)
* [pytest-django 4.4.0](https://pypi.org/project/pytest-django/)
* [djangorestframework-simplejwt 4.7.2](https://pypi.org/project/djangorestframework-simplejwt/)
* [Pillow 9.2.0](https://pypi.org/project/Pillow/)
* [PyJWT 2.1.0](https://pypi.org/project/PyJWT/)
* [requests 2.26.0](https://pypi.org/project/requests/)

## Как запустить проект:

* Клонировать репозиторий и перейти в него в командной строке

```
git clone git@github.com:LevLM/infra_sp2.git
cd infra_sp2
```

* Переходим в папку с файлом docker-compose.yaml:

```
cd infra
```

* Разворачиваем образы и сразу запускаем проект infra из 3 контейнеров (db_1, web_1, nginx_1):

```
docker-compose up -d --build
```

* Выполняем миграции:

```
docker-compose exec web python manage.py migrate
```

* Создаем суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

* Подключаем статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

* Заполняем базу исходными данными:

```
docker-compose exec web python manage.py loaddata fixtures.json
```

* Создаем дамп (резервную копию) базы:

```
docker-compose exec web python manage.py dumpdata > fixtures.json
```

* Загрузить в базу данные из дампа (файл fixtures.json разместить в папке с Dockerfile):

```
docker-compose exec web python manage.py loaddata fixtures.json
```

* Проверяем работоспособность приложения:

```
 http://localhost/admin/
```

## Шаблон наполнения env-файла (виртуальное окружение):

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=admin
POSTGRES_PASSWORD=ghbdtn11
DB_HOST=db
DB_PORT=5432

Данные внести в файл ".env", поместить его в папке Infra (где находится файл docker-compose.yaml)


## Документация для YaMDb доступна по адресу:

```http://127.0.0.1/redoc/```