from flask import Blueprint, request, jsonify, jsonify
import datetime
from app.api.v1.meetups import models as ObjMeetUps

meetups_class = ObjMeetUps.Meetups()

meetups = Blueprint('meetups', __name__, url_prefix='/api/v1')

""" Refer to this response spec for rsvp
{
“status” : Integer,
    “data” : [
        {
                “meetup” : Integer, // meetup record primary key
                “topic” : String, // meetup topic
                “status”: String // [yes, no or maybe]
    }
]"""

meetup_rsvp = []
# route to rsvp a meetup
@meetups.route("/meetups/<int:meetup_id>/rsvps", methods=['POST'])
def rsvp(meetup_id):
    data = request.get_json()
    Id = data['meetup_id']
    topic = ['topic']
    status = ['status']
    
    if data:
        rsvp_rec = {'id': Id, 'topic': topic, 'status': status}
        meetup_rsvp.append(rsvp_rec)
        #call the method to add the rsvp
        return jsonify({"status": 201, "data": data})

#post a meetup
@meetups.route("/meetups", methods=['POST'])
def post_meetup():
    data = request.get_json()
    topic = data['topic']
    location = data['location']
    happeningOn = datetime.datetime.now()
    tags = data['tags']
    
    if data:
        new_meetup={'topic': topic, 'location': location, 'happeningOn': happeningOn, 'tags': tags}
        # meetups_class.save()
        return jsonify({"status": 201, 'data': new_meetup}), 201

# test funtion to return all meetup records
@meetups.route("/meetups", methods=['GET'])
def get_all_meetup():
    # return jsonify(meetups_class.all()), 200
    return jsonify({ 'status': 200, 'data': meetups_class.all()}), 200

#fetch a specific meetup record
@meetups.route("/meetups/<int:meetupId>", methods=['GET'])
def get_meetup(meetupId):
    # Testing using postman to return the json string - to replace with method in meetups models class Meetups
    # return jsonify({"message": "route to fetch a question"})
    return jsonify({"status": 200, "data": meetups_class.find_by_id(meetupId)}), 200

@meetups.route("/meetups/upcoming/", methods=['GET'])
def get_upcoming():
    #fetch all upcoming meetups
    return jsonify({"status": 200, "data": meetups_class.upcoming()}), 200
