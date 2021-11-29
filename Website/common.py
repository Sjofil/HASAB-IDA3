import functools

from flask.helpers import make_response
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
        stmt="SELECT * FROM user WHERE Adress =%s"
        cursor.execute(stmt, username)
        user=cursor.fetchone()
        if user is None:
            print(stmt)
            print(user)
            error = 'Ogiltig email.'
        
        if error is None:
            session.clear()
            #saves the id in the session for future safety checks.
            session['user_id'] = user[0]
            print(session['user_id'])
            session['questions'] = get_questions(user[1])
            response = make_response(redirect(url_for('questions.questionMain')))
            response.set_cookie('answers', '', expires=0)
            return response

        flash(error)
    return render_template("index.html")

def get_questions(typeID):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM questions WHERE Type_ID=%s", typeID)
    questions = cursor.fetchall()

    questionIDs = []
    for question in questions:
        questionIDs.append(str(question[0]))

    delimiter = ","
    delimiter = delimiter.join(questionIDs)

    #Detta bör vara säkert från SQL-injektion då detta sker på servern enbart
    cursor.execute("SELECT * FROM conditional_question WHERE question_id IN (" + delimiter + ")")
    conditional = cursor.fetchall()
    print(conditional)
    return questions

