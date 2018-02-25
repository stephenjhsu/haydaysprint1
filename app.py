from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return "Hello World"

application.run(host='0.0.0.0',port=8080,debug=True)
