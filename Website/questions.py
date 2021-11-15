from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from . import db

bp = Blueprint('questions', __name__, url_prefix='/')


@bp.route("/question", methods = ['GET', 'POST'])
def questionMain():
    if request.method == 'GET':
        #questionIndex = request.args.get('page')
        cursor = db.get_db().cursor()
        questions = cursor.execute('SELECT * FROM questions WHERE Type_ID=1').fetchall()
        return questions
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

@bp.route("/Admin-html/amdmin-log-in-html")
def start():
    return render_template("ad.html")    