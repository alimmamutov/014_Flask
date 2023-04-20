"""
Здесь второй вариант запуска приложени через фабрику приложений
"""

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from blog.config import Development


db = SQLAlchemy()
login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Development())
    db.init_app(app)  # здесь связали бд с приложением
    from .models import User

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    from blog.report.views import report
    from blog.user.views import user
    from blog.article.views import article
    from blog.auth.views import auth
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
    app.register_blueprint(auth)


