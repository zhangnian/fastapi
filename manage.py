from flask_script import Manager

from fastapi import app, db

manager = Manager(app)


@manager.command
def createdb(drop_db = False):
    if drop_db:
        db.drop_all()
    db.create_all()


@manager.command
def runserver():
    app.run(port=8191, debug=True)


if __name__ == '__main__':
    manager.run()
    #runserver()