from flask import Flask, render_template, request, redirect, url_for
from main_code import main_code  # Import your function
import requests,time

app = Flask(__name__)
WEB_APP_URL = 'https://7d6f-110-39-215-194.ngrok-free.app/'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    session_id = request.form['session_id']
    
    print(username,password,session_id) 
    response_obj = main_code(username, password,session_id)
    
    return response_obj
        
if __name__ == '__main__':
    app.run(debug=True)