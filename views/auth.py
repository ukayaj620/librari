from flask import Blueprint, request, render_template, jsonify, session, redirect, url_for, flash
from db.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User

auth = Blueprint('auth', __name__, template_folder='templates', url_prefix='/auth')

@auth.route('/signin')
def signin():
  return render_template('signin.html')

@auth.route('/signup')
def signup():
  return render_template('signup.html')

@auth.route('/login', methods=['POST'])
def login():
  user = User().fetch(request.form['email'])
  if user and check_password_hash(user['password'], request.form['password']):
    session['name'] = user['firstname'] + ' ' + user['lastname']
    session['id'] = user['id']
    session['loggedIn'] = True
  else:
    flash('Wrong password or email', 'danger')

  return redirect(url_for('index'))

@auth.route('/logout', methods=['GET'])
def logout():
  session.pop('name', None)
  session.pop('email', None)
  session.pop('loggedIn', None)
  return redirect(url_for('index'))

@auth.route('/register', methods=['POST'])
def register():
  user = User()
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