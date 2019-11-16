# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/10/31 0:20"

from flask import current_app

from httper import HTTP

class YuShuBook:
    """
        从api获取数据
    """
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        res = HTTP.get(url)
        self._fill_single(res)
        # 不再返回，而是将数据记录在类实例
        # return res

    def search_by_keyword(self, q, page):
        url = self.keyword_url.format(q, current_app.config['PER_PAGE'], self.calculate_start(page))
        res = HTTP.get(url)
        self._fill_colletion(res)
        # 不再返回，而是将数据记录在类实例
        # return res

    def _fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def _fill_colletion(self, data):
        self.total = data['total']
        self.books = data['books']

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']