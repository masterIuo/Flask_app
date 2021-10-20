from flask import *

from forms import LoginForm

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/basic')

@app.route('/basic')
def basic():
    form = LoginForm()
    return render_template('basic_form.html',form=form)


if __name__ == '__main__':
    app.run()