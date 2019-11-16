# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/11/15 2:54"

# 处理返回数据
class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages']
        self.author = book['author']
        self.price = book['price']
        self.summary = book['summary']
        self.image = book['image']

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]

"""
class BookViewModel:

    @classmethod
    def package_single(cls, data, keyword):
        returned =  {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = cls.__cut_response_data(data)
        return returned

    @classmethod
    def package_colletion(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_response_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_response_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'] or '',
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
"""