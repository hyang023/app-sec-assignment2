#import flask
from flask import Flask
#create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on
app = Flask(__name__)

#the route() decorator tells Flask what URL should trigger our function
@app.route('/')
def hello_world():
    return 'Hello, World!'

#citation: http://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
