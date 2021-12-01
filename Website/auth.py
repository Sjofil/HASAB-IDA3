import functools
from sqlite3 import dbapi2

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask.wrappers import Request
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
        if (session['user_id'] != 'Admin'):
            return redirect(url_for('auth.login'))

    if request.method == 'POST':
        if(session['user_id'] != 'Admin' or request.form['submit']=="logOut"):
            print("clearing session")
            session.clear()
            return redirect(url_for('auth.login'))
        if(request.form['submit']=="addUser"):
            print(request.form)
            stmt="INSERT INTO `user` (`Type_ID`, `Adress`, `Name`) VALUES (%s, %s, %s)"
            print(stmt)
            conn=db.get_db()
            cursor=conn.cursor()
            cursor.execute(stmt, (request.form['branch'], request.form['adress'], request.form['name']))
            conn.commit()
            
        # Sammanställ rapport av de olika branscherna
        if(request.form['submit']=="Resturang"):    
            return redirect(url_for('auth.reportTemplate'))
        if(request.form['submit']=="Hotell"):
            return redirect(url_for('auth.reportTemplate'))
        if(request.form['submit']=="Byrå"):
            return redirect(url_for('auth.reportTemplate'))
        if(request.form['submit']=="Anläggning"):
            return redirect(url_for('auth.reportTemplate'))
    
        if(request.form['submit']=="changePassword"):
            if(request.form['pass1']==request.form['pass2']):
                stmt="UPDATE `admin` SET `password` = %s WHERE (`name` = %s)"
                conn=db.get_db()
                cursor=conn.cursor()
                cursor.execute(stmt, (request.form['pass1'], session['user_id']))
                conn.commit()
            else :
                error="lösen matchade ej"
                flash(error)
    
        # Om admin sökt en enskild rapport 
        if(request.form['submit']=="findReport"):
            name = request.form['name']
            #if (ifPresent("Name", name)):
            print(request.form)
            stmt = "SELECT distinct Question_text, Value, Name from answers, questions, user \
             where questions.ID = Question_ID and Name = (%s)"
            conn=db.get_db()
            cursor=conn.cursor()
            print(stmt)
            print("hit funkar det") # yes hit funkar det
            cursor.execute(stmt, (request.form['name']))
            records = cursor.fetchall()
            print(records)
            for row in records:
                print(row[0], " = ", row[1])
        
    return render_template("Admin-html/admin-index.html")
    
            


def ifPresent(column, value):
    conn = db.get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * from user WHERE (%s) = (%s)", (column, value))
    return cursor.fetchone() is not None
        
