from flask import Flask, jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q：关键字
        page：页数
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        res = YuShuBook.search_by_isbn(q)
    else:
        res = YuShuBook.search_by_keyword(q)

    return jsonify(res)
    # return json.dumps(res), 200, {'content-type':'application/json'}




if __name__ == '__main__':

    app.config.from_object('config')
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)
