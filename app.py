from flask import Flask, render_template, request
app = Flask(__name__)

unamelist = [] 
pwordlist = [] 
twofalist = [] 

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
 
        if uname  and pword :
        	if uname in unamelist:
        	    message="Failure: username already exists"
        	else:
        	    unamelist.append(uname)
        	    pwordlist.append(pword)
        	    if twofa.isdigit():
        	        twofalist.append(twofa)
        	    else:
        	        twofalist.append('no')
        	    message = "Success"

    return render_template('registration.html', message=message)

@app.route('/login',  methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        uname = request.form.get('uname')
        pword = request.form.get('pword')
        twofa = request.form.get('2fa')
 
        if uname  and pword :
        	message = "Incorrect"
        	if uname in unamelist:
        	    index = unamelist.index(uname)
        	    message = "uname index: "+index
        	    if pword == pword[index]:
        	        message = "Success"
        	        #message = "Incorrect uname is "+unamelist[i]+" and pword is "+pwordlist[i]+" but you entered user: "+uname+" and pass: "+pword

    return render_template('login.html', message=message)

@app.route('/login_success', methods=['POST'])
def login_success():
    return render_template('login_success.html')

@app.route('/spell_check', methods=['post', 'get'])
def spell_check():
    message = ''
    message2 = ''
    if request.method == 'POST':
        inputtext = request.form.get('inputtext')
 
        if inputtext:
            message = "Supplied Text: "
            message2 = "Misspelled words: "
    return render_template('spellcheck.html', message=message, message2=message2)
