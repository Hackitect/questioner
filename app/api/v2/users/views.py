from flask import Blueprint, request, json, jsonify

users = Blueprint('users', __name__, url_prefix='/api/v2')

@users.route('/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if data:
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        username = data['username']
        phonenumber = data['phonenumber']
        password = data['password']
