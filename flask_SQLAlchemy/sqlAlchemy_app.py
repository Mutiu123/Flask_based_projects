import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Get the parent directory path
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

# Initialize Flask app with custom template and static folder paths
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Configure SQLAlchemy with SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

# Define User model (use 'flask shell' to create the database and 'db.create_all()' to create the tables. 
# # use 'exit()' to exit the shell. Then use 'User model' to add data)
# use 'sqlite3 instance\db.sqlite3' to view the database, 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    date_joined = db.Column(db.DateTime)

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