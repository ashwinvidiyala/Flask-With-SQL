import re, md5
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')
app.secret_key = 'VerySecretKey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']
    hashed_password = md5.new(password).hexdigest()
    error = 0

    match = re.search(r'[a-zA-Z][a-zA-Z]+', first_name)
    if match:
        pass
    else:
        error += 1
        flash('First name should be letters only and have at least 2 characters.')

    match = re.search(r'[a-zA-Z][a-zA-Z]+', last_name)
    if match:
        pass
    else:
        error += 1
        flash('Last name should be letters only and have at least 2 characters.')

    match = re.search(r'[^@]+@[^@]+\.[^@]+', email)
    if match:
        pass
    else:
        error += 1
        flash('Email address is not valid')

    if len(password) >= 8:
        pass
    else:
        error += 1
        flash('Password is not long enough')

    if password == password_confirmation:
        pass
    else:
        error += 1
        flash('Passwords do not match.')

    if error == 0:
        query = "INSERT INTO users_login (first_name, last_name, email, password, password_confirmation, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :password_confirmation, NOW(), NOW())"
        data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': hashed_password,
        'password_confirmation': hashed_password,
        }
        mysql.query_db(query, data)
        return render_template('success.html')
    else:
        return redirect('/')

app.run(debug = True)
