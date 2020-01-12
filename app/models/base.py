# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2020/1/1 23:10"

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger


db = SQLAlchemy()

class Base(db.Model):
    # 不希望创建基类模型，设置__abstract__为True
    __abstract__ = True
    # create_time = Column('create_time', Integer)
    # 软删除标志
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for k,v in attrs_dict.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)