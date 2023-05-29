#-*- encoding: utf-8 -*-
#!/usr/bin/blog_venv python3.7
"""
[File]        : models.py
[Time]        : 2023/05/27 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 1.0
[Description] : Database model.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 1.0"

from extends import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(36), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)

class ArticleModel(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship(UserModel, backref="articles")

class CommentModel(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    article = db.relationship(ArticleModel, backref=db.backref("comments", order_by=create_time.desc()))
    author = db.relationship(UserModel, backref=db.backref("comments", order_by=create_time.desc()))

