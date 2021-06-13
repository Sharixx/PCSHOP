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


@app.route('')


if __name__ == "__main__":
    app.run(debug=True)
