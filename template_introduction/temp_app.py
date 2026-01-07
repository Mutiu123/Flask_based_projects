import os
from flask import Flask, render_template

# Get the parent directory path
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

# Create the Flask application instance with custom template and static folder paths
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Root route: simple greeting
@app.route('/')
def welcome():
    return "<h1>Hello, World!</h1>"

@app.route('/home')
def home():
    return 'Hello, Flask! Welcome to the Flask Application.'


@app.route('/index')
def index():
    return render_template('index.html')

# paas variable to template
@app.route('/variables')
def variables():
    return render_template('index.html', name="Adesina", age=25)

@app.route('/condition')
def condition():
    return render_template('cond.html', name="Mutiu", age=65, data=[{"key": "value1"}, {"key": "value2"}, {"key": "value3"}])  # Change age to test different groups