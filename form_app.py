from flask import *

from forms import LoginForm

app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = '2ch3D9h38SG5v43UE98hc781DGHB34'


@app.route('/')
def home():
    return "home"


@app.route('/hello')
def index():
    return 'Hello form'


@app.route('/basic', methods=['GET', 'POST'])
def basic():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        flash('Welcome home,%s' % username)
        return redirect(url_for('hello'))
    return render_template('basic_form.html', form=form)


if __name__ == '__main__':
    app.run()
