# _*_ coding: utf-8 _*_
from flask import Flask

__author__ = "吴飞鸿"
__date__ = "2019/11/1 18:08"

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)