# Flask
## Мамутов Алим 
***
***Практическое задание***

**Урок 1. Знакомство: werkzeug, Flask**
1. Создайте новый проект на github.
2. Начните новый проект и установите Flask.
3. Cоздайте базовый index view для обработки посещений на корень сайта.
4. Cдайте работу в виде ссылки на репозиторий с кодом.
***

**Урок 2. Шаблоны Jinja2. Комплексные приложения на Flask. Blueprints** 
1. Добавить в свой проект на Flask использование шаблонов и стилей Bootstrap.
2. В базовый шаблон добавить навигационную панель, которая будет отображаться на всех страницах ресурса.
3. Реализовать страницы со списком доступных статей и пользователей, а также возможность перехода к их деталям.
***

**Урок 3. Авторизация пользователя и начало работы с базой данных. SQLAlchemy**
1. Подключить Flask-SQLAlchemy в свой Flask проект.
2. Создать базовую модель пользователя, добавить к ней UserMixin.
3. Добавить страницу авторизации.
4. Создать один view, который недоступен анонимным пользователям.




# Demo App - Quick start

## Install 
1. Create new virtual env
```shell
python3 -m venv ./venv
```
2. copy `example.env` to `.env` and set `SECRET_KEY`
3. activate virtual env
```shell
source venv/bin/activate
```
4. install dependencies
```shell
pip install -r requirements.txt
```
5. Run command for init db and create user
```shell
flask init-db
flask create-init-user
```
6. Run flask application
```shell
flask run
```