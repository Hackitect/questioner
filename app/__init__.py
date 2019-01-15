from flask import Flask
import psycopg2
from psycopg2 import Error

    
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = ""

    try:
        db = psycopg2.connect(
            user = "questioner",
            password = "password123",
            host = "localhost",
            port = '5432',
            database  = "questioner"
        )
        
    except (Exception, psycopg2.DatabaseError) as Error:
        raise Error

    from app.api.v1.meetups.views import meetups
    from app.api.v1.questions.views import questions

     
    # db.init_app(app)

    #register the blueprints

    app.register_blueprint(meetups)
    app.register_blueprint(questions)

    return app