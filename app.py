from flask import Flask, render_template, redirect, url_for, session
from db.db import db
from views.auth import auth
import credentials

app = Flask(__name__)
app.secret_key = credentials.SECRET_KEY

app.config['MYSQL_DATABASE_USER'] = credentials.DB_USERNAME
app.config['MYSQL_DATABASE_PASSWORD'] = credentials.DB_PASSWORD
app.config['MYSQL_DATABASE_DB'] = credentials.DB_DBNAME
app.config['MYSQL_DATABASE_HOST'] = credentials.DB_HOSTNAME
db.init_app(app)

app.register_blueprint(auth, url_prefix='/auth')

@app.route('/')
def index():
  if 'loggedIn' in session and session['loggedIn'] == True:
    return render_template('home.html')
  return redirect(url_for('auth.signin'))


if __name__ == '__main__':
  app.run(debug=True)
