import re
from types import NoneType
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
        if page>len(session["questions"]):
            return redirect(url_for("questions.questionThree"))

    return render_template("question1.html", 
    questionObject=session["questions"], 
    page=max(1, min(page, len(session["questions"]))))

@bp.route("/question2")
def questionTwo():
    return render_template("question2.html")   

@bp.route("/question2-2")
def questionTwoTwo():
    return render_template("question2-2.html")   

@bp.route("/send-form" , methods=['GET','POST'])
def questionThree():
    if request.method == 'POST':
        if request.is_json:
            jsonData = request.get_json()
            connection = db.get_db()
            cursor = connection.cursor()
            for answer in jsonData:
                cursor.execute("INSERT INTO answers (Value, Question_ID, User_id) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE Value=VALUES(Value)"
                , (jsonData[answer], answer, session['user_id']))

            connection.commit()
            return redirect(url_for('questions.last'))

    return render_template("send-form.html")

@bp.route("/last")
def last():
    return render_template("last.html")  

@bp.route("/Admin-html/amdmin-log-in-html")
def start():
    return render_template("ad.html")    