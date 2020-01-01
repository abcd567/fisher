# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2020/1/1 23:10"



from sqlalchemy import Column, Integer, String, Boolean, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base

class Gift(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 关联用户模型
    user_ = relationship('User')
    uid = Column(Integer, ForeignKey('user_.id'))
    # 关联书籍，因为isbn可以识别唯一的一本书，不必再用外键模型关联。但这本书有可能有多本，所以isbn在这里不能是唯一
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)


