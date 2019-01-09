from flask import Blueprint, request, jsonify, jsonify
import datetime
from app.api.v1.meetups import models as ObjMeetUps

meetups_class = ObjMeetUps.Meetups()

meetups = Blueprint('meetups', __name__, url_prefix='/api/v1')

#post a meetup
@meetups.route("/meetups", methods=['POST'])
def post_meetup():
    return jsonify({"message": "route to post a meetup"}), 201

# test funtion to return all meetup records
@meetups.route("/meetups", methods=['GET'])
def get_all_meetup():
    return jsonify(meetups_class.all())

#fetch a specific meetup record
@meetups.route("/meetups/<int:meetupId>", methods=['GET'])
def get_meetup(meetupId):
    # Testing using postman to return the json string - to replace with method in meetups models class Meetups
    # return jsonify({"message": "route to fetch a question"})
    return jsonify(meetups_class.find_by_id(meetupId))