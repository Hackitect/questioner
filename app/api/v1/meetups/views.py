from flask import Blueprint, request, jsonify, jsonify
import datetime
from app.api.v1.meetups import models as ObjMeetUps

meetups_class = ObjMeetUps.Meetups()

meetups = Blueprint('meetups', __name__, url_prefix='/api/v1')

#post a meetup
@meetups.route("/meetups", methods=['POST'])
def post_meetup():
    data = request.get_json()
    if data:
        topic = data[topic] #e.g. "Ubuntu Server Hangout"
        location = data['location'] #e.g. The Hub"
        happeningOn = datetime.date.now() # "2019, 2, 8, 7, 50, 55, 529588"
        tags = data['tags'] #e.g. ["linux", "server"]

        new_meetup={'topic': topic, 'location': location, 'happeningOn': happeningOn, 'tags': tags}

    return jsonify({"status": 201, 'data': meetups_class.new(new_meetup)}), 201

# test funtion to return all meetup records
@meetups.route("/meetups", methods=['GET'])
def get_all_meetup():
    # return jsonify(meetups_class.all()), 200
    return jsonify({ 'status': 200, 'data': meetups_class.all()})

#fetch a specific meetup record
@meetups.route("/meetups/<int:meetupId>", methods=['GET'])
def get_meetup(meetupId):
    # Testing using postman to return the json string - to replace with method in meetups models class Meetups
    # return jsonify({"message": "route to fetch a question"})
    return jsonify(meetups_class.find_by_id(meetupId))

@meetups.route("/meetups/upcoming/", methods=['GET'])
def get_upcoming():
    #fetch all upcoming meetups
    return jsonify(meetups_class.upcoming())
