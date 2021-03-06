# _*_ coding: utf-8 _*_
from flask import Flask
from flask_login import LoginManager

from app.models.base import db

__author__ = "吴飞鸿"
__date__ = "2019/11/1 18:08"

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或者注册'

    # db.create_all(app=app)
    with app.app_context():
        db.create_all()
    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)