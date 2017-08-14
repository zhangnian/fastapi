import sys

from fastapi import app, db



def create_db():
    with app.app_context():
        db.create_all()
        db.session.commit()


if __name__ == '__main__':
    sys.argv.append('run')

    if 'createdb' in sys.argv[1]:
        create_db()
    else:
        app.run(port=8191, debug=True)