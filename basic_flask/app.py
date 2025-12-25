# ...existing code...
from flask import Flask, render_template, request, redirect, url_for

# Create the Flask application instance
app = Flask(__name__) 

# Root route: simple greeting
@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

# Route with uppercase path segment: demonstrates different route names
@app.route('/Home')
def home_Uppercase():
    return "<h1>Hello, World! This is my Home uppercase page.</h1>"

# Route that returns JSON (Flask will jsonify dicts automatically)
@app.route('/json')
def json():
    return {"name": "John", "age": 30, "city": "New York"} 

# Route that supports both GET and POST
@app.route('/home', methods=['GET', 'POST'])
def home():
    # Handle form submission (POST)
    if request.method == 'POST':
        return "<h1>Form Submitted!</h1>"
    
    # Handle normal page view (GET)
    return "<h1>Hello, World! This is my home page.</h1>" 

# Dynamic route with a default value for user_input
@app.route('/dynamic', defaults={'user_input': 'Guest'})
@app.route('/dynamic/<user_input>')
def dynamic(user_input):
    # user_input comes from the URL or defaults to 'Guest'
    return f"<h1>Hello, {user_input}! Welcome to your dynamic page.</h1>" 

# Route that reads query string parameters
@app.route("/query")
def query():
    first = request.args.get("first_name")   # ?first_name=...
    last  = request.args.get("last_name")    # ?last_name=...
    return f"<h1>This is the query string contains: firstname: {first} and lastname: {last}</h1>" 
# Example: http://127.0.0.1:5000/query?first_name=Mutiuand&last_name=Adegboye 

# Simple form route that reads form data
@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user_input = request.form.get('user_input')  # read form field
        return f"<h1>You entered: {user_input}</h1>"                                                                                                    
    # Render a minimal form for GET requests
    return '<form method="POST"><input type="text" name="user_input" /><input type="submit" /></form>' 

# Route that accepts JSON payloads (typically sent with application/json)
@app.route('/acceptjson', methods=['POST', 'GET'])
def accessjson():
    # Parse JSON body; request.get_json() returns None if no JSON present
    json_data = request.get_json()
    first_name = json_data.get('api_input1') if json_data else 'No data received'
    last_name = json_data.get('api_input2') if json_data else 'No data received'
    Favourite_number = json_data.get('api_input3') if json_data else 'No data received'
    # Return a multi-line HTML response with each value separated
    return f"""
<h1>This is the JSON data you sent:</h1>
<p>First Name: {first_name}</p>
<p>Last Name: {last_name}</p>
<p>Favourite Number: {Favourite_number}</p>
""" 

# Route demonstrating redirect after POST (Post/Redirect/Get pattern)
@app.route("/form_redirect", methods=['GET', 'POST'])
def form_redirect():
    if request.method == 'POST':
        user_input = request.form['user_input']  # read required form field
        print(user_input)                        # log to stdout (visible in console)
        return redirect(url_for('form_redirect'))# redirect to same route (GET)
    return '<form method="POST"><input type="text" name="user_input" /><input type="submit" /></form>'

# Route that intentionally raises an error to demonstrate error handling
@app.route('/error')
def error():
    c = 1/0  # intentional ZeroDivisionError
    return "Error"
# ...existing code...