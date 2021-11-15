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
        stmt="SELECT * FROM user WHERE Adress ='" + username + "'"
        cursor.execute(stmt)
        user=cursor.fetchone()
        if user is None:
            print(stmt)
            print(user)
            error = 'Ogiltig identifieringskod.'
        
        if error is None:
            session.clear()
            #saves the id in the session for future safety checks.
            session['user_id'] = user[3]
            print(session['user_id'])
            return redirect(url_for('questions.questionMain'))

        flash(error)
    return render_template("index.html")

@bp.route("/login")
def login():
    return render_template("Admin-html/admin-log-in.html")

@bp.route("/admin")
def index():
    return render_template("Admin-html/admin-index.html")