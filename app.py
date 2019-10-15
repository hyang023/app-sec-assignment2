from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/register', methods=['post', 'get'])
def register():
    message = ''
    if request.method == 'POST':
        uname = request.form.get('uname')
        pword = request.form.get('pword')
        twofa = request.form.get('2fa')
 
        if uname and pword:
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
