from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__) 

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/Home')
def home_Uppercase():
    return "<h1>Hello, World! This is my Home uppercase page.</h1>"

@app.route('/json')
def json():
    return {"name": "John", "age": 30, "city": "New York"} 


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # This part runs when the user submits data (e.g., clicking a button)
        return "<h1>Form Submitted!</h1>"
    
    # This part runs when the user just visits the page (GET request)
    return "<h1>Hello, World! This is my home page.</h1>" 


@app.route('/dynamic',defaults={'user_input': 'Guest'})
@app.route('/dynamic/<user_input>')
def dynamic(user_input):
    return f"<h1>Hello, {user_input}! Welcome to your dynamic page.</h1>" 

#
@app.route("/query")
def query():
    first=request.args.get("first_name")
    last = request.args.get("last_name")
    return f"<h1>This is the query string contains: firstname: {first} and lastname: {last}</h1>" 
# http://127.0.0.1:5000/query?first_name=Mutiuand&last_name=Adegboye 

# send data via form
@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        return f"<h1>You entered: {user_input}</h1>"                                                                                                    
    return '<form method="POST"><input type="text" name="user_input" /><input type="submit" /></form>' 

@app.route('/acceptjson')
def accessjson():
    json_data = request.get_json()
    first_name = json_data.get('api_input1') if json_data else 'No data received'
    last_name = json_data.get('api_input2') if json_data else 'No data received'
    Favourite_number = json_data.get('api_input3') if json_data else 'No data received'
    return f"""
<h1>This is the JSON data you sent:</h1>
<p>First Name: {first_name}</p>
<p>Last Name: {last_name}</p>
<p>Favourite Number: {Favourite_number}</p>
""" 

@app.route("/form_redirect", methods=['GET', 'POST'])
def form_redirect():
    if request.method == 'POST':
        user_input = request.form['user_input']
        print(user_input)
        return redirect(url_for('form_redirect'))
    return '<form method="POST"><input type="text" name="user_input" /><input type="submit" /></form>'

@app.route('/error')
def error():
    c = 1/0
    return "Error"