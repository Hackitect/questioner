from flask import Blueprint, request, json, jsonify

users = Blueprint('users', __name__, url_prefix='/api/v2')

@users.route('/auth/signup', methods=['POST'])
def signup():
    pass