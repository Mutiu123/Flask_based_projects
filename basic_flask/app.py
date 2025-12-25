from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/Home')
def home():
    return "<h1>Hello, World! This is my home page.</h1>"

@app.route('/json')
def json():
    return {"name": "John", "age": 30, "city": "New York"} 

@app.route('/Home', methods=['GET'])
def home():
    return "<h1>Hello, World! This is my home page.</h1>"