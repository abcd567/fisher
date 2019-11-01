# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/11/1 18:48"

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)