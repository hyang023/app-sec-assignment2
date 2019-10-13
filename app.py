from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register')
def register():
    return 'registration page'

@app.route('/login')
def login():
    return 'login page'

@app.route('/spell_check')
def spell_check():
    return 'spell_check page'
