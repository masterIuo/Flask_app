from urllib.parse import urlparse, urljoin

from flask import *

app = Flask(__name__)

app.secret_key = 'masterluo'

def redirect_back(default='hello', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


@app.route('/goback/<int:year>')
def go_back(year):
    return 'Welcome to %d!' % (2021 - year)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
    return '<h1>Hello, %s</h1>' % name


colors = ['red', 'black', 'yellow']


# @app.route('/colors/<any(%s):color>' % str(colors)[1:-1])
@app.route('/colors/<any(red,black,yellow):color>')
def colors(color):
    return '<h1>Like %s?</h1>' % color


@app.route('/redir')
def redir():
    return redirect('https://www.huya.com')


@app.route('/404')
def not_found():
    abort(404)


@app.route('/foo')
def foo():
    return '<h1>Foo page</h1><a href="%s">do something</a>' % url_for('do_something')


@app.route('/bar')
def bar():
    return '<h1>Bar page><a href="%s">Do something </a>' % url_for('do_something')


@app.route('/note')
def note():
    data = {
        'name': 'masterluo',
        'age': 20,
        'gender': 'male'
    }
    res = make_response(json.dumps(data))
    res.mimetype = 'application/json'
    return res


@app.route('/set/<name>')
def set_cookie(name):
    res = make_response(redirect(url_for('hello')))
    res.set_cookie('name', name)
    return res


@app.route('/do_something_and_redirect')
def do_something():
    return redirect_back()

@app.route('/flash')
def just_flash():
    flash('hello!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
