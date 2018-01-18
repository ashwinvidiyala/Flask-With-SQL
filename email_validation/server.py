from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')
app.secret_key = 'VerySecretKey'

@app.route('/')
def index():
    return render_template('index.html', valid_email = session['valid'])

@app.route('/create', methods=['POST'])
def create():
    db_email_query = "SELECT email FROM emails WHERE email = :email"
    db_email_data = {'email': request.form['email']}
    db_email = mysql.query_db(db_email_query, db_email_data)
    print db_email
    if len(db_email) == 0:
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {'email': request.form['email']}
        mysql.query_db(query, data)
        return redirect('/success')
    elif db_email[0]['email'] == request.form['email']:
        flash('Email is not valid')
        return redirect('/')

@app.route('/success')
def success():
    emails = mysql.query_db("SELECT * FROM emails")
    return render_template('success.html', all_emails = emails)

app.run(debug =True)
