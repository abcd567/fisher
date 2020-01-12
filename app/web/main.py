
from . import web





# def __current_user_status_change():
#     r = request


@web.route('/')
# @cache.cached(timeout=100, unless=__current_user_status_change)
# @cache.cached(timeout=100)
def index():
    return '首页'


@web.route('/personal')
# @login_required
def personal_center():
    pass


