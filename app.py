from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register')
def hello_world():
    return render_template('registration.html')

@app.route('/login')
def hello_world():
    return 'login page'

@app.route('/spell_check')
def hello_world():
    return 'spell_check page'
