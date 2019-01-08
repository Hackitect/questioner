from flask import Blueprint, request, jsonify, jsonify
import datetime
from app.api.v1.meetups import models

meetups = Blueprint('meetups', __name__, url_prefix='/api/v1')

#post a meetup
@meetups.route("/meetups", methods=['POST'])
def post_meetup():
    return jsonify({"message": "route to post a meetup"})

#fetch a specific meetup record
@meetups.route("/meetups/<int:meetupId>", methods=['GET'])
def get_meetup(meetupId):
   return jsonify({"message": "route to fetch a question"})