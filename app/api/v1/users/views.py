from flask import Blueprint, request, json, jsonify
from app.api.v1.users import models

auth = Blueprint('auth', __name__, url_prefix='/api/v1')

user_object = models.Users()

