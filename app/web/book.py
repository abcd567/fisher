# _*_ coding: utf-8 _*_
from flask import jsonify, request

__author__ = "吴飞鸿"
__date__ = "2019/11/1 18:14"

from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from app.forms.book import SearchForm

@web.route('/book/search/')
def search():
    """
        q：关键字
        page：页数
        ?q=西游记&page=1
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            res = YuShuBook.search_by_isbn(q)
        else:
            res = YuShuBook.search_by_keyword(q, page)

        return jsonify(res)
    else:
        return jsonify(form.errors)