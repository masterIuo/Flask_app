from flask import *

user = {
    'username': 'masterluo',
    'bio': 'A god'
}

movies = [
    {'name': 'totoro', 'year': '1988'},
    {'name': 'colors', 'year': '1993'},
    {'name': 'matrix', 'year': '1997'}
]

app = Flask(__name__)

app.secret_key = 'masterluo'

@app.route('/movie')
def movie():
    return render_template('watchlist.html', user=user, movies=movies)

@app.route('/')
def index():
    return '<p>Hello movie</p>'

@app.template_filter()
def musical(s):
    return s + Markup(' &#9835;')

def bar():
    return 'I am bar'
foo = 'I am foo'

def baz(name):
    if name == 'baz':
        return True
    return False

@app.route('/flash')
def just_flash():
    flash('I am flash!')
    return redirect(url_for('index1'))

@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404



app.jinja_env.globals['bar'] = bar   # 直接传函数名表示这个对象
app.jinja_env.globals['foo'] = foo
app.jinja_env.filters['musical'] = musical
app.jinja_env.tests['baz'] = baz

if __name__ == '__main__':
    app.run()
