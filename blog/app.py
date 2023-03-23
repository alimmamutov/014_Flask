from urllib import response

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


@app.route("/greet/<name>/")
def greet_name(name: str):
    return f"Hello {name}!"


'''
> http://127.0.0.1:5000/user/
User [no name] [no surname]
> http://127.0.0.1:5000/user/?name=John&surname=Smith
User John Smith
'''
@app.route("/user/")
def read_user():
    name = request.args.get("name")
    surname = request.args.get("surname")
    return f"User {name or '[no name]'} {surname or '[no surname]'}"


@app.route('/status', methods=['GET', 'POST'])
def custom_status_code():
    if request.method == 'GET':
        return 'You use get method', 404

    print('raw bytes data:', request.data)

    if request.form and 'code' in request.form:
        return 'code from form', request.form['code']
    if request.json and 'code' in request.json:
        return 'code from json', request.json['code']
    return '', 204
