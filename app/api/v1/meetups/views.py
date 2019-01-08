from flask import Blueprint, request, jsonify, jsonify
import datetime
from app.api.v1.meetups import models

meetups = Blueprint('meetups', __name__, url_prefix='/api/v1')

#post a meetup
@meetups.route("/meetups", methods=['POST'])
def post_meetup():
    pass

#fetch a specific meetup record
@meetups.route("/meetups/<meetup-id>", methods=['GET'])
def get_meetup():
    pass