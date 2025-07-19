from flask import Flask, render_template, request, redirect, url_for, session
import subprocess
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user storage for demonstration
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email in users and users[email] == password:
        session['user'] = email
        return redirect(url_for('dashboard'))
    return "Invalid credentials, please try again."

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    users[email] = password  # Store user credentials
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    return redirect(url_for('index'))

@app.route('/start')
def start():
    # Start the AI_Main.py script
    process = subprocess.Popen(['python', 'AI_Main.py'])
    return "AI Assistant is running."

@app.route('/shutdown')
def shutdown():
    # This will close the AI process and then show a thank you message
    os.system("taskkill /f /im python.exe")  # Forcefully kill all python processes
    return "Thank you for Using Virtual Assistant Desktop."

if __name__ == '__main__':
    app.run(debug=True)