from flask import Flask, request, render_template, jsonify
from flaskext.mysql import MySQL
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

@app.route('/login', methods=['POST'])
def login():
  user = User(conn=conn).fetch(request.form['email'])
  if user and check_password_hash(user['password'], request.form['password']):
    # TODO: redirect to home, add session
    return jsonify({'message': 'Password is correct'})
  
  return jsonify({'error': 'User or password are incorrect'}), 401


@app.route('/register', methods=['POST'])
def register():
  user = User(conn=conn).fetch(request.form['email'])
  if user:
    return jsonify({'message': 'Email has been registered, please proceed to login'}), 400
  else:
    if User(
      firstname=request.form['firstname'],
      lastname=request.form['lastname'],
      email=request.form['email'],
      password=generate_password_hash(request.form['password']),
      conn=conn
    ).create(): return jsonify({'message': 'User has registered successfully'})

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')

if __name__ == '__main__':
  app.run(debug=True)