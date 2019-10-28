from flask import Flask, make_response

# from config import DEBUG

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hhh')
def hhh():
    headers = {
        'content-type': 'text/html; charset=utf8',
        'location': 'http://www.baidu.com',  # 301 重定向
    }
    return '<html>装饰器实质上返回的是一个response对象, 返回值是body, status code, headers等</html>', 301, headers

# 不适用装饰器的路由方式，配合app.add_url_rule使用；装饰器本身就是通过add_url_rule来实现的
def aaa():
    headers = {
        'content-type': 'text/html; charset=utf8',
        # 'location': 'http://www.baidu.com', # 301 重定向 在这里需要处理重定向的url，不然不能重定向去别的网站
    }
    response = make_response('<html>装饰器实质上返回的是一个response对象</html>', 404)
    response.headers = headers
    return response
    # return '<html>这样默认的content-type 是 text/plain, 而且 xianshi zhongwen hui luanma, 因为charset没设置utf8 </html>'


if __name__ == '__main__':
    app.add_url_rule('/aaa', view_func=aaa)
    # 导入配置文件的另一种方法
    app.config.from_object('config')
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)
