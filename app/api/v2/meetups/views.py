from flask import Blueprint, request, jsonify, session

meetups = Blueprint('meetups', __name__, url_prefix='/api/v2')

#route to delete a meetup using meetup id
@meetups.route("/meetups/<int:meetup_id>", methods=['DELETE'])
# @admin_required
def delete():
    pass
