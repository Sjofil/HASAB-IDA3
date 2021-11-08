import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

#from flaskr.db import get_db

bp = Blueprint('questions', __name__, url_prefix='/')


@bp.route("/question1")
def questionOne():
    return render_template("question1.html")

@bp.route("/question2")
def questionTwo():
    return render_template("question2.html")   

@bp.route("/question2-2")
def questionTwoTwo():
    return render_template("question2-2.html")   

@bp.route("/send-form")
def questionThree():
    return render_template("send-form.html")

@bp.route("/last")
def last():
    return render_template("last.html")  

@bp.route("/start")
def start():
    return render_template("start.html")    