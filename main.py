from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return ('<h1>Hallo Welt!!</h1>')

app.run(debug=True, port=9876)