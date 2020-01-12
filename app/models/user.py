# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2020/1/1 23:10"


from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.models.base import Base
from app import login_manager


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    # 密文密码_password
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    # 读取
    @property
    def password(self):
        return self._password

    # 赋值
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 从明文密码验证密文密码
    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    # # 使用flask_login插件，需要加上get_id函数
    # def get_id(self):
    #     return self.id
    # 或者继承UserMixin，就不再需要写get_id函数了（当然，如果不用id表示用户身份，还是需要重写get_id函数的）

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))