# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/11/4 21:03"

from sqlalchemy import Column, Integer, String

from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(32), default='佚名')
    isbn = Column(String(15), nullable=False, unique=True)
    title = Column(String(50), nullable=False)
    summary = Column(String(1000))
    image = Column(String(50))
    publisher = Column(String(50))
    binding = Column(String(20))
    pages = Column(String(20))
    price = Column(String(20))
    pubdate = Column(String(20))


    def sample(self):
        pass