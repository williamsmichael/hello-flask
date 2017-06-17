from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title> | mdw</title>
    <meta name="description" content="Portland LaunchCode LC101">
    <meta name="author" content="mdw">
    <style>
        body {
            background: #333;
            color: #eee;
        }
    </style>
</head>
<body>
    <form action="/hello">
        <label for="first-name">First Name:</label>
        <input id="first-n ame" type="text" name="first_name">
        <input type="submit">
    </form>
</body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/hello")
def hello():
    first_name = request.args.get('first_name')
    return '<h1 style="color:#333;font-family:sans-serif;text-align:center;padding-top:20px">Hello, ' + first_name + '!</h1>'

app.run()