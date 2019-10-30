# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/10/31 0:20"

from httper import HTTP

class YuShuBook:
    """
        从api获取数据
    """
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        res = HTTP.get(url)
        return res

    @classmethod
    def search_by_keyword(cls, q, count=15, start=0):
        url = cls.keyword_url.format(q, count, start)
        res = HTTP.get(url)
        return res