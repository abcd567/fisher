# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/10/30 23:21"

def is_isbn_or_key(q):
    """
    判断搜索关键字是isbn还是key
    :param q:
    :return:
    """
    # isbn13 13位0-9数字；isbn10 10位0-9数字，中间含有 '-'
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    if '-' in q:
        short_q = q.replace('-', '')
        if len(short_q) == 10 and short_q.isdigit():
            isbn_or_key = 'isbn'
    return isbn_or_key