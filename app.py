from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

    if __name__ == '__main__':
        app.run(host=os.environ.get('IP','0.0.0.0'),
            port=os.environ.get('PORT','8888'),
            debug=True)
