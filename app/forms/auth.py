# _*_ coding: utf-8 _*_
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models.user import User

__author__ = "吴飞鸿"
__date__ = "2020/1/8 16:13"


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[DataRequired(message='密码不可为空'), Length(6, 32)])

    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称2-10个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮箱已注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')
    # 注：class Form 中有以下代码用于验证参数 ，所以上述验证函数名写成 validate_参数名
    """
        def validate(self):
        \"\"\"
        Validates the form by calling `validate` on each field, passing any
        extra `Form.validate_<fieldname>` validators to the field validator.
        \"\"\"
        extra = {}
        for name in self._fields:
            inline = getattr(self.__class__, 'validate_%s' % name, None)
            if inline is not None:
                extra[name] = [inline]

        return super(Form, self).validate(extra)
    """

class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[DataRequired(message='密码不可为空'), Length(6, 32)])