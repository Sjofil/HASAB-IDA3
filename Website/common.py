import functools
from . import db
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

#from flaskr.db import get_db

bp = Blueprint('common', __name__, url_prefix='/')

@bp.route("/", methods=('GET', 'POST'))
def main():
    if request.method == 'POST':
        username = request.form['id-check']
        db1=db.get_db()
        error = None
        cursor=db1.cursor()
        cursor.execute("SELECT * FROM user WHERE Name ='" + username + "'" )
        user=cursor.fetchone()
        if user is None:
            error = 'Ogiltig identifieringskod.'
        
        if error is None:
            session.clear()
            session['user_id'] = user[3]
            return redirect(url_for('questions.questionOne'))

        flash(error)
    return render_template("index.html")

@bp.route("/login")
def login():
    return render_template("Admin-html/admin-log-in.html")

@bp.route("/admin")
def index():
    return render_template("Admin-html/admin-index.html")