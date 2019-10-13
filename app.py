from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register')
def hello_world():
    return 'registration page'

@app.route('/login')
def hello_world():
    return 'login page'

@app.route('/spell_check')
def hello_world():
    return 'spell_check page'
