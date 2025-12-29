import os
from flask import Flask, render_template

# Get the parent directory path
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/index')
def index():
    return render_template('index.html')

# paas variable to template
@app.route('/variables')
def variables():
    return render_template('index.html', name="Mutiu", age=15)

@app.route('/condition')
def condition():
    return render_template('cond.html', name="Mutiu", age=35)  # Change age to test different groups