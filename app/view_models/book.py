# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/11/15 2:54"

# 处理返回数据
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