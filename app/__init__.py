from flask import Flask
import psycopg2

    
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = ""

    try:
        connection = psycopg2.connect(
            user = "questioner",
            password = "password123",
            host = "localhost",
            port = '5432',
            database  = "questioner"
        )
        cursor = connection.cursor
    except (Exception, psycopg2.Error) as Error:
        return Error

    from app.api.v1.meetups.views import meetups
    from app.api.v1.questions.views import questions

     
    

    #register the blueprints

    app.register_blueprint(meetups)
    app.register_blueprint(questions)

    return app