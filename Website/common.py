import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

#from flaskr.db import get_db

bp = Blueprint('common', __name__, url_prefix='/')

@bp.route("/index")
def main():
    return render_template("index.html")