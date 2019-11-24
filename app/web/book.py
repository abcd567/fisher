# _*_ coding: utf-8 _*_
import json

from flask import jsonify, request, flash, render_template

from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection

__author__ = "吴飞鸿"
__date__ = "2019/11/1 18:14"



@web.route('/book/search')
def search():
    """
        q：关键字
        page：页数
        ?q=西游记&page=1
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # 用jsonify()参数不能是对象,所以用json, 需要设置一下返回头
        headers = {
            'content-type': 'application/json; charset=utf8',
        }
        # return json.dumps(books, default= lambda o: o.__dict__), 200, headers
    else:
        # return jsonify(form.errors)
        flash('搜索的关键字不符合要求，请重新输入')

    return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass