class User:
  def __init__(self, username=None, password=None, cursor=None):
    self.username = username
    self.password = password
    self.cursor = cursor

  def find_by_username(self, username):
    data = self.cursor.execute('SELECT * FROM users WHERE username = %s', (username))
    return dict(self.cursor.fetchone())
