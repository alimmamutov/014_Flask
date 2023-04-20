from enum import unique

from flask_login import UserMixin
from sqlalchemy.orm import relationship

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password =db.Column(db.String(255))


# class Article(db.Model):
#     __tablename__ = 'articles'
#     title = db.column(db.String(255))
#     text = db.column(db.String)
#     author = relationship('User')