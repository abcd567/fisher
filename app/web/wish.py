from . import web

def limit_key_prefix():
    pass

@web.route('/my/wish')
# @login_required
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
# @login_required
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
# @login_required
# @limiter.limit(key_func=limit_key_prefix)
def satisfy_wish(wid):
    """
        向想要这本书的人发送一封邮件
        注意，这个接口需要做一定的频率限制
        这接口比较适合写成一个ajax接口
    """
    pass


@web.route('/wish/book/<isbn>/redraw')
# @login_required
def redraw_from_wish(isbn):
    pass

