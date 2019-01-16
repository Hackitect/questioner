from flask import Blueprint, request, json, jsonify
from app.api.v1.users import models
import datetime

auth = Blueprint('auth', __name__, url_prefix='/api/v1')

user_object = models.Users()

@auth.route
def sign_up_user():
    data = request.get_json()
    if data:
        email = data['email']
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        password = data['password']
        timestamp = datetime.datetime.now()

        resp = jsonify(user_object.signup(email, firstname, lastname, username, password, timestamp)), 201
        return resp