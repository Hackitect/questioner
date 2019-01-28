import os
from instance.config import app_config
from flask import Flask
from flask_bcrypt import Bcrypt 


bcrypt = Bcrypt() # Encryption function


def create_app():
    app = Flask(__name__)
    # to get big random characters, start python interpreter, import secrets module, then 
    # use secrets.token_hex() method and pass in 24bytes to genrate a random string 
    app.config['JWT_SECRET_KEY'] = '9a231f01574449fd12a4f4dcde53abb3a3d384cdb0367086'

    #import the blueprints for our routes
    # from app.api.v1.meetups.views import meetups
    from app.api.v2.meetups.views import meetups as MeetV2
    from app.api.v1.questions.views import questions
    from app.api.v2.users.views import users
    from app.api.v1.users.views import auth

    bcrypt.init_app(app)
    #register the blueprints
    app.register_blueprint(MeetV2)
    app.register_blueprint(questions)
    app.register_blueprint(users)
    app.register_blueprint(auth)
   
    return app