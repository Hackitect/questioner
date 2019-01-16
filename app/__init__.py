from flask import Flask


def create_app():
    app = Flask(__name__)

    #import the blueprints for our routes
    from app.api.v1.meetups.views import meetups
    from app.api.v1.questions.views import questions
    from app.api.v2.users.views import users
    from app.api.v1.users.views import auth


    #register the blueprints
    app.register_blueprint(meetups)
    app.register_blueprint(questions)
    app.register_blueprint(users)
    app.register_blueprint(auth)
    return app