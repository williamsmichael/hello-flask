from flask import Flask, request, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Class 2.4 | mdw</title>
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
    <form action="/hello" method="post">
        <label for="first-name">First Name:</label>
        <input id="first-name" type="text" name="first_name">
        <input type="submit">
    </form>
</body>
</html>
"""

time_form = """
    <style>
        .error {{ color: red;}}
    </style>
    <h1>Validate Time</h1>
    <form method="POST">
        <label>Hours (24-hour format)
            <input type="text" name="hours" value='{hours}'>
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input type="text" name="minutes" value='{minutes}'>
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="Convert">
    </form>
    """

@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='', minutes='', minutes_error='')


def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


@app.route('/validate-time', methods=['POST'])
def validate_time():
    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range (0-23)'
            hours = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

    if not hours_error and not minutes_error:
        time = str(hours) + ':' + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))
    else:
        return time_form.format(hours_error=hours_error, minutes_error=minutes_error, hours=hours, minutes=minutes)

@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return """
    <h1>Valid Time</h1>
    <p>You submitted {0}. Thanks for submitting a valid time!</p>
    """.format(time)


@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return """
    <style>
        body {
            color: #333;
            font-family: sans-serif;
            text-align: center;
            padding-top: 20px
        }
    </style>
    <h1>Hello, """ + cgi.escape(first_name) + """ !</h1>
    """


@app.route("/")
def index():
    return form

app.run()