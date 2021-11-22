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
        jsonData = request.get_json()
        connection = db.get_db()
        cursor = connection.cursor()
        for i in range(0, len(jsonData)):
            try:
                jsonSplit = jsonData[i].split('=')
                questionID = jsonSplit[0]
                questionValue = jsonSplit[1]
                cursor.execute("INSERT INTO answers (Value, Question_ID, User_id) VALUES (%s, %s, %s)"
                , (questionValue, questionID, session['user_id']))
            except:
                print("Type is not string")

        connection.commit()
        return redirect(url_for('questions.last'))

    return render_template("send-form.html")

@bp.route("/last")
def last():
    return render_template("last.html")  

@bp.route("/Admin-html/amdmin-log-in-html")
def start():
    return render_template("ad.html")    