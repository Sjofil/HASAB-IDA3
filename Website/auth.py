import functools
from re import search
from sqlite3 import dbapi2
from pymysql.err import OperationalError

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask.wrappers import Request
import pymysql
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route("/reportTemplate")
def reportTemplate2():
    return render_template("Admin-html/reportTemplate.html")

@bp.route("/reportTemplate", methods= ('POST', 'GET'))
def reportTemplate():
    if (request.method == 'GET'):
        return render_template("Admin-html/reportTemplate.html")

def ifPresent(column, value):
    conn = db.get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE (%s) = (%s)", (column, value))
    return cursor.fetchone() is not None
        

@bp.route("/admin", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password=request.form['password']
        db1=db.get_db()
        cursor=db1.cursor()
        error = None
        stmt="SELECT * FROM Admins WHERE Username =%s AND Password=%s"
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

        if(request.form['submit'] == "deleteAnswers"):
            stmt="DELETE FROM Answers"
            conn=db.get_db()
            cursor=conn.cursor()
            cursor.execute(stmt)
            conn.commit()
            error="Alla svar från användarna togs bort"
            flash(error)

        if(request.form['submit'] == "removeUser"):
           
            stmt="DELETE FROM Users WHERE Email=(%s)"
            conn=db.get_db()
            cursor=conn.cursor()

            try:
                    cursor.execute(stmt, request.form['adress'])
                    conn.commit()
                    error="Användaren: " + request.form['adress'] + " togs bort"
                    flash(error)
            except pymysql.IntegrityError :
                error="Användaren: " + request.form['adress'] + "finns inte i systemet"
                flash(error)


        if(request.form['submit']=="addUser"):
           
            stmt="INSERT INTO Users (Type_ID, Email, Name) VALUES (%s, %s, %s)"
            print(stmt)
            conn=db.get_db()
            cursor=conn.cursor()
            try:
                if(request.form['name'] == ''):
                    name = None
                else:    
                    name = request.form['name']

                if(request.form['branch'] == 0):
                    branch = None
                else:
                    branch = request.form['branch']
                
                cursor.execute(stmt, (branch, request.form['adress'], name))
                conn.commit()
            except pymysql.IntegrityError as e:
                error="Emailadressen:  " + request.form['adress'] + " finns redan i systemet"
                flash(error)
                
            finally:
                cursor.close

           
            
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
                stmt="UPDATE Admin SET Password = %s WHERE (Username = %s)"
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
            print(name)
            stmt = "SELECT Name FROM Users WHERE Name LIKE CONCAT('%%', %s, '%%')" #Tror inte ni fattar hur lång tid detta tog
            conn=db.get_db()
            cursor=conn.cursor()
            print(stmt)
            print("hit funkar det") # Fungerar om man söker på nästan rätt namn. 
            cursor.execute(stmt, name)
            records = cursor.fetchall()
            print(records)     
            return redirect(url_for('auth.reportTemplate'), hehe = records)        
    return render_template("Admin-html/admin-index.html")


#Hämta svaren från databasen, visa i reportTemplate
@bp.route('/reportTemplate', methods = ['GET', 'POST'])
def reportTemplate3():
    conn = db.get_db()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Answers")
    data = cursor.fetchall()

    return render_template("reportTemplate.html", data = data)
            

