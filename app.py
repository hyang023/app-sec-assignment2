from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.rout('/login_success')
def login_success():
	return render_template('login_success.html')

@app.route('/spell_check')
def spell_check():
    return 'spell_check page'
