from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


@app.route("/")
def index():
    template = jinja_env.get_template('hello_form.html')
    return template.render(title="hello_form")


@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template('hello_greeting.html')
    return template.render(title="hello_greeting", first_name=first_name)


@app.route('/validate-time')
def display_time_form():
    template = jinja_env.get_template('time_form.html')
    return template.render(title="time_form")


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
        if hours not in range(24):
            hours_error = 'Hour value out of range (0-23)'
            hours = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes not in range(60):
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

    if not hours_error and not minutes_error:
        time = str(hours) + ':' + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))
    else:
        template = jinja_env.get_template('time_form.html')
        return template.render(title="time_form", hours_error=hours_error, minutes_error=minutes_error, hours=hours, minutes=minutes)


@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    template = jinja_env.get_template('valid_time.html')
    return template.render(title="valid_time", time=time)


tasks = []

@app.route('/todos', methods=['GET', 'POST'])
def todos():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    template = jinja_env.get_template('todos.html')
    return template.render(title="TODOs", tasks=tasks)

app.run()