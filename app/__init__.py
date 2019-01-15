from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.api.v1.meetups.views import meetups
    from app.api.v1.questions.views import questions

    #register the blueprints

    app.register_blueprint(meetups)
    app.register_blueprint(questions)

    return app