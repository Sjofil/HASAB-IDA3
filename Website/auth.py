import functools
from sqlite3 import dbapi2

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route("/admin", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password=request.form['password']
        db1=db.get_db()
        cursor=db1.cursor()
        error = None
        stmt="SELECT * FROM admin WHERE Name =%s AND password=%s"
        print(stmt)
        cursor.execute(stmt,(username, password))
        user=cursor.fetchone()
        if user is None:
            error = 'Ogiltig identifieringskod.'
        
        if error is None:
            session.clear()
            session['user_id'] = user[0]
            print(session['user_id'])
            return redirect(url_for('auth.adminLoggedIn'))

        flash(error)

    return render_template('Admin-html/admin-log-in.html')


# Checks if admin is logged in. If not - /admin is rendered
@bp.route("/adminIndex", methods=('GET', 'POST'))
def adminLoggedIn():
    if request.method == 'GET':
        if (session['user_id'] == 'Admin'):
            return render_template('Admin-html/admin-index.html')
        
        
    return render_template('Admin-html/admin-log-in.html')
        
