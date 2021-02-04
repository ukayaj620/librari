from flask import Flask, request, render_template
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)


# refactor needed
# db connection should be created as a class on a seperated file
db = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'librari'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
db.init_app(app)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)