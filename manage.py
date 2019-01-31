from flask_script import Manager
from app.api.v2.utils.database import Database
from app import create_app

app = create_app()
db = Database()
manager = Manager(app)

@manager.command
def create_tables():
    db.create_tables()

if __name__ == '__main__':
    manager.run()