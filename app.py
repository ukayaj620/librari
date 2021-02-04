from flask import Flask, request, render_template, jsonify
from flaskext.mysql import MySQL
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User

app = Flask(__name__)

db = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'librari'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
db.init_app(app)

conn = db.connect()
cursor = conn.cursor(pymysql.cursors.DictCursor)

@app.route('/login', methods=['POST'])
def login():
  user = User(cursor=cursor).find_by_username(request.form['username'])
  if user and check_password_hash(user['password'], request.form['password']):
    # TODO: redirect to home, add session
    return jsonify({'message': 'Password is correct'})
  
  return jsonify({'error': 'User or password are incorrect'}), 401


@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)