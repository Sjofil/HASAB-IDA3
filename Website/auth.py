import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route("/")
def login():
    if request.method == 'POST':
        username = request.form['Användarnamn']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        
        if user is None:
            error = 'Ogiltigt användarnamn.'
        
        if error is None:
            session.clear()
            session['user_id'] = user['']
        )