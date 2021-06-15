from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/account')
def account():
    return render_template('account.html')


@app.route('/pcbuilds')
def pcbuilds():
    return render_template('pcbuilds.html')


@app.route('/periphery')
def periphery():
    return render_template('periphery.html')


@app.route('/complementary')
def complementary():
    return render_template('complementary.html')


@app.route('/basket')
def basket():
    return render_template('basket.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
