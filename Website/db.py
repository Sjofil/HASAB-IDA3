
from flaskext.mysql import MySQL
from flask import current_app, g
from flask.cli import with_appcontext
import click


def get_db():
    if'db' not in g:
        mysql=MySQL()
        current_app.config['MYSQL_DATABASE_USER'] = 'fi5004sj'
        current_app.config['MYSQL_DATABASE_PASSWORD'] = 'f601lghw'
        current_app.config['MYSQL_DATABASE_DB'] = 'fi5004sj'
        current_app.config['MYSQL_DATABASE_HOST'] = 'vm23.cs.lth.se'
        mysql.init_app(current_app)
        g.db=mysql.connect()
        return g.db

def close_db(e=None):
    db=g.pop('db',None)
    if db is not None:
        db.close()
       

def init_db():
    db = get_db()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')       

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)