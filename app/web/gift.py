from . import web
from flask_login import login_required


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
# @login_required
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
# @login_required
def redraw_from_gifts(gid):
    pass
