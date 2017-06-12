from flask import Flask

app = Flask(__name__)
app.config['DEBUG']

@app.route("/")
def index():
    return "Hello World"

app.run()