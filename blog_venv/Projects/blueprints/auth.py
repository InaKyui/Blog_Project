import random
import string
from .forms import RegisterForm, LoginForm
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from models import UserModel
from extends import db, mail, cache
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint(name="auth", import_name=__name__, url_prefix="/auth")

@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱不存在")
                return redirect(url_for("auth.login"))
            else:
                if check_password_hash(user.password, password):
                    session["user_id"] = user.id
                    return redirect(url_for("qa.index"))
                else:
                    print("密码错误")
                    return redirect(url_for("auth.login"))
        else:
            return redirect(url_for("auth.login"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data

            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            cache.delete(email)
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))

@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    captcha = "".join(random.sample(string.digits * 4, 4))
    cache.set(email, captcha, timeout=180)
    message = Message(subject="Blog test.", recipients=[email], sender="3023667843@qq.com", body=captcha)
    mail.send(message)
    return jsonify({"code":200, "message":"", "data":None})