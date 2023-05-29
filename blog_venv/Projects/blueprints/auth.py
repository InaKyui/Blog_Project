#-*- encoding: utf-8 -*-
#!/usr/bin/blog_venv python3.7
"""
[File]        : auth.py
[Time]        : 2023/05/27 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 1.0
[Description] : Blueprint auth.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 1.0"

import random
import string
from flask import Blueprint, jsonify, redirect, render_template, url_for, request, session, g
from models import UserModel
from extends import db, mail, cache
from werkzeug.security import check_password_hash, generate_password_hash
from blueprints.forms import LoginForm, RegisterForm
from flask_mail import Message

bp = Blueprint(name="auth", import_name=__name__, url_prefix="/auth")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth_login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                # User does not exist.
                return redirect(url_for("auth.login"))
            else:
                if check_password_hash(user.password, password):
                    # Correct password.
                    session["user_id"] = user.id
                    return redirect(url_for("index.homepage"))
                else:
                    # Wrong password.
                    return redirect(url_for("auth.login"))
        else:
            # Wrong form formatting.
            return redirect(url_for("auth.login"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("auth_register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            # Clear email captcha cache.
            cache.delete(email)
            return redirect(url_for("auth.login"))
        else:
            return redirect(url_for("auth.register"))

@bp.route("/logout")
def logout():
    g.user = None
    session.clear()
    return redirect(url_for("auth.login"))

@bp.route("/send_captcha")
def send_captcha():
    email = request.args.get("email")
    # Generate random captcha.
    captcha = "".join(random.sample(string.digits * 4, 4))
    cache.set(email, captcha, timeout=180)
    body = "Hello esteemed user,\r\n\r\n\
                You are creating a user account for InaKyui blog. \r\n\
                Your verification code is {}.\r\n\
                Please input it within 3 minutes.\r\n\r\n\
            Thank you for your support.".format(captcha)
    # Send captcha email.
    message = Message(
        subject="InaKyui Blog - Email verification code.",
        recipients=[email],
        sender=mail.username,
        body=body)
    mail.send(message)
    return jsonify({"code":200, "message":"", "data":None})