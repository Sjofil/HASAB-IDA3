from flask import (
    Blueprint, render_template
)

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route("/mailing")
def mailingPage():
    return render_template("Admin-html/admin-mail-list.html")