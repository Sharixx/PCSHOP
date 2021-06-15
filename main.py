from flask import Flask, render_template

app = Flask(__name__)


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
