from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'fullfriendsdb')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT *, DATE_FORMAT(friend_since, '%M %e %Y') as friend_since_formatted FROM friends")
    return render_template('index.html', all_friends = friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (name, age, friend_since, created_at, updated_at) VALUES (:name, :age, :friend_since, NOW(), NOW())"
    data = {
            'name': request.form['name'],
            'age': request.form['age'],
            'friend_since': request.form['friend_since']
           }
    mysql.query_db(query, data)
    return redirect('/')

# @app.route('/friends/<friend_id>')
# def show(friend_id):
#     query = "SELECT * FROM friends WHERE id = :specific_id"
#     data = {'specific_id': friend_id}
#     friends = mysql.query_db(query, data)
#     return render_template('index.html', one_friend = friends[0])

app.run(debug=True)
