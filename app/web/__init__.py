# _*_ coding: utf-8 _*_
from flask import Blueprint

__author__ = "吴飞鸿"
__date__ = "2019/11/1 18:12"

# 注册蓝图
web = Blueprint('web', __name__)

# 导入模块(必须导入模块，里面的代码才会执行，而且必须先注册蓝图后导入)；或者可以把注册蓝图单独放一个文件，再在book里面改变web导入的位置，防止循环导入
from app.web import book
from app.web import auth
from app.web import main
from app.web import wish
from app.web import gift
from app.web import drift

