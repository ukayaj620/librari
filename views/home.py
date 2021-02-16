from flask import Blueprint, request, render_template, jsonify, session, redirect, url_for, flash
from db.db import db
from models.book import Book
from .helpers.check_session import check_session

home = Blueprint('home', __name__, template_folder='templates', url_prefix='/home')

@home.route('/')
@check_session
def index():
  return render_template('home/book.html')

@home.route('/category')
@check_session
def category():
  return render_template('home/category.html')