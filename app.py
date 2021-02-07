from flask import Flask, request, render_template, jsonify, session, redirect, url_for, flash
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
import credentials

app = Flask(__name__)
app.secret_key = credentials.SECRET_KEY

db = MySQL()
app.config['MYSQL_DATABASE_USER'] = credentials.DB_USERNAME
app.config['MYSQL_DATABASE_PASSWORD'] = credentials.DB_PASSWORD
app.config['MYSQL_DATABASE_DB'] = credentials.DB_DBNAME
app.config['MYSQL_DATABASE_HOST'] = credentials.DB_HOSTNAME
db.init_app(app)

conn = db.connect()

@app.route('/login', methods=['POST'])
def login():
  user = User(conn=conn).fetch(request.form['email'])
  if user and check_password_hash(user['password'], request.form['password']):
    session['name'] = user['firstname'] + ' ' + user['lastname']
    session['id'] = user['id']
    session['loggedIn'] = True
  else:
    flash('Wrong password or email', 'danger')

  return redirect(url_for('index'))

@app.route('/logout', methods=['GET'])
def logout():
  session.pop('name', None)
  session.pop('email', None)
  session.pop('loggedIn', None)
  return redirect(url_for('index'))


@app.route('/register', methods=['POST'])
def register():
  user = User(conn=conn)
  data = user.fetch(request.form['email'])
  if data:
    flash('Email has been registered, please proceed to login', 'info')
  else:
    if user.create({
      'firstname': request.form['firstname'],
      'lastname': request.form['lastname'],
      'email': request.form['email'],
      'password': generate_password_hash(request.form['password']),
    }):
      flash('Data has been registered, please login', 'success')
  
  return redirect(url_for('index'))

@app.route('/')
def index():
  if 'loggedIn' in session and session['loggedIn'] == True:
    return render_template('home.html')
  return render_template('index.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')


if __name__ == '__main__':
  app.run(debug=True)
