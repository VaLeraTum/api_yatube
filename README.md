# API для Yatube

### Описание

Проект Yatube - это социальная сеть, где можно вести свой дневник, подписываться на понравившихся авторов, комментировать их посты и создавать тематические группы.

### Стек технологий

* Python 3.9.10,
* Django 3.2.16,
* DRF,
* JWT

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ValeraTum/api_yatube.git
```

```
cd yatube_api
```

Создать и активировать виртуальное окружение:

```
python3 -m venv venv
```
* Если у вас Linux/macOS

```
source venv/bin/activate
```
* Если у вас windows

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Установить Djoser
```

pip install djoser djangorestframework-simplejwt==4.7.2
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

### В проекте доступны эндпоинты:

Для неавторизованных пользователей работа с API доступна только в режиме чтения.

```r
api/v1/posts/ - Для работы с постами 
api/v1/posts/{post_id}/comments/ - Для работы с комментариями 
api/v1/groups/ - Для работы с группами
api/v1/follow/ - Для работы с подписками
api/v1/jwt/ - Для работы с JWT
