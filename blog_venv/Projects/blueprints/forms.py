import wtforms
from models import UserModel
from extends import cache
from wtforms.validators import Email, Length, EqualTo

# Verify that the data submitted by the front-end meets the requirements.
class RegisterForm(wtforms.Form):
    # 格式验证。
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="验证码格式错误！")])
    username = wtforms.StringField(validators=[Length(min=4, max=16, message="")])
    password = wtforms.StringField(validators=[Length(min=6, max=16, message="")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    # 自定义验证。
    def validate_email(self, filed):
        email = filed.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="改邮箱已经被注册")

    def validate_captcha(self, filed):
        captcha = filed.data
        email = self.email.data

        try:
            if not cache.get(email) == captcha:
                raise wtforms.ValidationError(message="验证码错误")
            else:
                print(email)
        except:
            raise wtforms.ValidationError(message="验证码错误")

class LoginForm(wtforms.Form):
    # 格式验证。
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=16, message="")])

