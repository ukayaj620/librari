import pymysql

class User:
  def __init__(self, firstname=None, lastname=None, email=None, password=None, conn=None):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.password = password
    self.conn = conn
    self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)


  def create(self):
    self.cursor.execute(
      'INSERT INTO users VALUES (NULL, %s, %s, %s, %s)', 
      (self.firstname, self.lastname, self.email, self.password)
    )
    self.conn.commit()
    return self.fetch(self.email)
    
    
  def fetch(self, email):
    data = self.cursor.execute('SELECT * FROM users WHERE email = %s', (email))
    return self.cursor.fetchone()
