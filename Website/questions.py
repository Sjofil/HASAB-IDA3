from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from . import db

bp = Blueprint('questions', __name__, url_prefix='/')


@bp.route("/question", methods = ['GET', 'POST'])
def questionMain():
    if request.method == 'GET':
        value=request.args.get('page')
        page=int(1 if value is None else value)

    if(page > 0):
        return render_template("question1.html", 
        questionObject=session["questions"], 
        page=page)
    else:
        error = "Ogilitigt sido nummer"
        flash(error)

    return render_template("question1.html", questionObject=None, page=page)

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

@bp.route("/Admin-html/amdmin-log-in-html")
def start():
    return render_template("ad.html")    