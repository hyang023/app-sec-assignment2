from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register')
def register():
	message = ''
	if request.method == 'POST':
        uname = request.form.get('uname')
        pword = request.form.get('pword')
        2fa = request.form.get('2fa')
 
        if username and password:
        #    message = "Correct username and password"
        #else:
            message = "Success"
    return render_template('registration.html', message=message)

@app.route('/register_success', methods=['POST'])
def register_success():
	return render_template('register_success.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_success', methods=['POST'])
def login_success():
	return render_template('login_success.html')

@app.route('/spell_check')
def spell_check():
    return 'spell_check page'
