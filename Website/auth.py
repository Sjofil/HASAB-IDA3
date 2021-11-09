import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from Website.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route("/auth")
def login():
    if request.method == 'POST':
        username = request.form['Identifieringskod:']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        
        if user is None:
            error = 'Ogiltig identifieringskod.'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('admin-log-in.html')


    
@bp.route("/auth")
def loginAdmin():
    if request.method == 'POST':
        username = request.form['Användarnamn:']
        password = request.form['Lösenord:']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM users WHERE username = ? AND type = 5', (username,)
        ).fetchone()
                

        if user is None:
            error = 'Felaktigt användarnamn.'
        elif not check_password_hash(user['password'], password):
            error = 'Felaktigt lösenord.'
                
        if error is None:
            session.clear()
            session['user_id'] = user['ID']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/admin-log-in.html')

        
