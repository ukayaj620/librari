import pymysql
from db.db import db

class User:
  def __init__(self):
    self.conn = db.connect()
    self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)


  def create(self, user=dict({})):
    self.cursor.execute(
      'INSERT INTO users VALUES (NULL, %s, %s, %s, %s)', 
      (user['firstname'], user['lastname'], user['email'], user['password'])
    )
    self.conn.commit()
    return self.fetch(user['email'])
    
    
  def fetch(self, email):
    data = self.cursor.execute('SELECT * FROM users WHERE email = %s', (email))
    return self.cursor.fetchone()
