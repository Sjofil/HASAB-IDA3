import functools
from sqlite3 import dbapi2

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route("/reportTemplate")
def reportTemplate():
    return render_template("Admin-html/reportTemplate.html")

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

        #Add user
        if(request.form['submit']=="addUser"):
            print(request.form)
            stmt="INSERT INTO `user` (`Type_ID`, `Adress`, `Name`) VALUES (%s, %s, %s)"
            print(stmt)
            conn=db.get_db()
            cursor=conn.cursor()
            cursor.execute(stmt, (request.form['branch'], request.form['adress'], request.form['name']))
            conn.commit()
            
            
        if(request.form['submit']=="Resturang"): #Value="Resturang", "Hotell", "Byrå", "Anläggning"          
            return redirect(url_for('auth.reportTemplate'))
        if(request.form['submit']=="Hotell"):
            return redirect(url_for('auth.reportTemplate'))
        if(request.form['submit']=="Byrå"):
            return redirect(url_for('auth.reportTemplate'))
        if(request.form['submit']=="Anläggning"):
            return redirect(url_for('auth.reportTemplate'))
    
    return render_template("Admin-html/admin-index.html")
    
            


        

        
