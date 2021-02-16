from flask import session, redirect, request, url_for, flash
from functools import wraps

def check_session(f):
  @wraps(f)
  def func(*args, **kwargs):
    if 'loggedIn' not in session:
      return redirect(url_for('auth.index'))
    return f(*args, **kwargs)
  return func