from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.api.v1.meetups.views import meetups

    #register the blueprints

    app.register_blueprint(meetups)

    return app