from flask import Flask, render_template, redirect, url_for, session, request
from db.db import db
from views.auth import auth
from views.home import home
import credentials
from views.helpers.check_session import check_session

app = Flask(__name__)
app.secret_key = credentials.SECRET_KEY

app.config['MYSQL_DATABASE_USER'] = credentials.DB_USERNAME
app.config['MYSQL_DATABASE_PASSWORD'] = credentials.DB_PASSWORD
app.config['MYSQL_DATABASE_DB'] = credentials.DB_DBNAME
app.config['MYSQL_DATABASE_HOST'] = credentials.DB_HOSTNAME
db.init_app(app)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(home, url_prefix='/home')

@app.route('/')
@check_session
def index():
  return redirect(url_for('home.index'))


if __name__ == '__main__':
  app.run(debug=True)
