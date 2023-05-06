"""
Здесь второй вариант запуска приложени через фабрику приложений
"""
from os import getenv, path
from json import load

from . import commands
from .extensions import db, login_manager
from flask import Flask

# from blog.config import Development         I changed class based config to env based conf
from .extensions import db, login_manager, migrate
from .article.views import article
from .index.views import index
from .models import User
from .user.views import user
# from .index.views import index
from .report.views import report
from .auth.views import auth

VIEWS = [
    index,
    user,
    article,
    report,
    auth
]


def create_app() -> Flask:
    app = Flask(__name__)
    # app.config.from_object(Development())
    app.config.from_object('blog.config')
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)
