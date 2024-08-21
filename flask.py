from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return'Hello World Welcome to Level 5 of Python Assignment'

if __name__ == '__main__':
    app.run()