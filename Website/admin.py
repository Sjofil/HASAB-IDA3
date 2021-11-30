import functools
from . import db
from flask import (
    Blueprint, g, render_template, redirect, render_template, request, session, url_for
)

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route("/mailing")
def mailingPage():
    return render_template("Admin-html/admin-mail-list.html")

""""
if request.method == "POST":
        connection = db.get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM answers")
        connection.commit()
        answers = cursor.fetchall()
        return render_template("Admin-html/reportTemplate.html", data = answers)
    else:
        return render_template("Admin-html/reportTemplate.html")
"""


@bp.route("/reportTemplate", methods = ["POST", "GET"])
def reportTemplate():
    return render_template("Admin-html/reportTemplate.html")