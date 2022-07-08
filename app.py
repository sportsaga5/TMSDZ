from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('main.html')


@app.route("/<name>", methods = ['GET', 'POST'])
def hello_for(name):
    if request.method == 'GET':
        return f'<h1>Hello, {name}!</h1>'

    elif request.method == 'POST':
        return request.get_json()


@app.route('/secret/')
def secret():
    return render_template('secret.html')
