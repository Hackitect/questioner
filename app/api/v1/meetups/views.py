from flask import Blueprint, request, jsonify, jsonify
import datetime
from app.api.v1.meetups import models

meetups = Blueprint('meetups', __name__)

#post a meetup
@meetups.route("/api/v1/meetups", methods=['POST'])
def post_meetup():
    pass