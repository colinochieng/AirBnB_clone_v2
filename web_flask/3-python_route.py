#!/usr/bin/python3
"""
script that starts a Flask web application:
- the web application listen on 0.0.0.0, port 5000
- Routes: /: display “Hello HBNB!”
- /hbnb: display “HBNB”
- /c/<text>: display “C ”
- /python/(<text>): display “Python ”
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """renders hello to home"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """Routing to hbnb page"""
    return "HBNB"

@app.route('/c/<text>')
def C_text(text):
    """
    display C followed by the value of the text variable
    """
    if '_' in text:
        text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<text>')
@app.route('/python/')
def py_txt(text='is cool'):
    """
    display Python, followed by the value of the text variable
    """
    if '_' in text:
        text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
