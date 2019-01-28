from flask import Blueprint, request, json, jsonify
from app.api.v2.users import models

#import the Users class from users.model 
# which defines the various methods to work with users views
user_object = models.Users()

users = Blueprint('users', __name__, url_prefix='/api/v2')

@users.route('/auth/signup', methods=['POST'])
def signup():
    # Test the route with simple return
    # return jsonify({"status": 201, "message": "User created successfully"}), 201
    data = request.get_json()
    if not request.json or not 'username' in request.json or not 'email' in request.json or not 'password' in request.json:
        return jsonify ({"label":"username, email and password fields required"}), 400
    if data:
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        username = data['username']
        phonenumber = data['phonenumber']
        password = data['password']

        return jsonify(user_object.save(firstname, lastname, email, username, phonenumber, password)), 201

@users.route('/auth/login', methods=['POST'])
def login():
    if not request.json or not 'email' in request.json or not 'password' in request.json:
        return jsonify ({"label":"you must enter both email and password"}), 400
    
    data = request.get_json()
    email = data['email']
    password = data['password']

    if data:
        #test whether values in the POST body are being captured
        # return jsonify({"Status": 201, "Message": "User logged in successfully", 
        #                 "email": email, "password": password}), 201
        return jsonify(user_object.login(email, password))
@users.route('/auth/users', methods=['GET'])
def get_all():
    return jsonify({"users": user_object.all()})

