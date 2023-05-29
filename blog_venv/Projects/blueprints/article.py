#-*- encoding: utf-8 -*-
#!/usr/bin/blog_venv python3.7
"""
[File]        : article.py
[Time]        : 2023/05/27 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 1.0
[Description] : Blueprint article.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 1.0"

from flask import Blueprint, render_template, request, redirect, url_for, g
from models import ArticleModel, CommentModel
from extends import db
from blueprints.forms import ArticleForm, CommentForm
from decorators import login_required

bp = Blueprint(name="article", import_name=__name__,  url_prefix="/article")

@bp.route("/")
def article():
    articles = ArticleModel.query.order_by(ArticleModel.create_time.desc()).all()
    return render_template("article.html", articles=articles)

@bp.route("/new", methods=["GET", "POST"])
@login_required
def new_article():
    if request.method == "GET":
        return render_template("article_new.html")
    else:
        form = ArticleForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            article = ArticleModel(title=title, content=content, author=g.user)
            db.session.add(article)
            db.session.commit()
            return redirect(url_for("article.article"))

@bp.route("/detail/<article_id>")
@login_required
def detail(article_id):
    article = ArticleModel.query.get(article_id)
    return render_template("article_detail.html", article=article)

@bp.post("/new/comment")
@login_required
def new_comment():
    form = CommentForm(request.form)
    if form.validate():
        content = form.content.data
        article_id = form.article_id.data
        comment = CommentModel(content=content, article_id=article_id, author_id=g.user.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("article.detail", article_id=article_id))
    else:
        return redirect(url_for("article.detail", article_id=request.form.get("article_id")))

@bp.route("/search")
def search():
    key = request.args.get("key")
    articles = ArticleModel.query.filter(ArticleModel.title.contains(key)).all()
    return render_template("article.html", articles=articles)