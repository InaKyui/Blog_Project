#-*- encoding: utf-8 -*-
#!/usr/bin/blog_venv python3.7
"""
[File]        : forms.py
[Time]        : 2023/05/27 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 1.0
[Description] : Form format.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 1.0"

import wtforms
from models import UserModel
from extends import cache
from wtforms.validators import Email, Length, EqualTo, InputRequired

class RegisterForm(wtforms.Form):
    # Define format.
    email = wtforms.StringField(validators=[Email(message="Incorrect email format!")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="Incorrect captcha format!")])
    username = wtforms.StringField(validators=[Length(min=4, max=16, message="Incorrect username format!")])
    password = wtforms.StringField(validators=[Length(min=6, max=16, message="Incorrect password format!")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password", message="Inconsistent passwords twice!")])

    # Custom validation.
    def validate_email(self, filed):
        email = filed.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="This email address has been registered!")

    def validate_captcha(self, filed):
        captcha = filed.data
        email = self.email.data

        try:
            if cache.get(email) != captcha:
                raise wtforms.ValidationError(message="Incorrect captcha!")
        except:
            raise wtforms.ValidationError(message="There are some errors in the email.")


class LoginForm(wtforms.Form):
    # Define format.
    email = wtforms.StringField(validators=[Email(message="Incorrect email format!")])
    password = wtforms.StringField(validators=[Length(min=6, max=16, message="Incorrect password format!")])


class ArticleForm(wtforms.Form):
    # Define format.
    title = wtforms.StringField(validators=[Length(min=1, max=36, message="Incorrect title format!")])
    content = wtforms.StringField(validators=[Length(min=1, message="Incorrect content format!")])


class CommentForm(wtforms.Form):
    # Define format.
    content = wtforms.StringField(validators=[Length(min=1, message="Incorrect content format!")])
    article_id = wtforms.IntegerField(validators=[InputRequired()])