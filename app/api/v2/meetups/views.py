from flask import Blueprint, request, jsonify, session
from app.api.v2.meetups import models

meetups = Blueprint('meetups', __name__, url_prefix='/api/v2')

# meet_obj = models.Meetup()

#route to delete a meetup using meetup id
@meetups.route("/meetups/<int:meetup_id>", methods=['DELETE'])
# @admin_required
def delete(meetup_id):
    return jsonify(models.Meetup.delete_meetup(meetup_id))

@meetups.route("/meetups/", methods=['POST'])
def create_meetup():
    data = request.get_json()
    if not data or not data['topic'] or not data['location'] or not data['happening_on']:
        return jsonify({"status": 400, "message": "missing some fields"})
    topic = data['topic'],
    location = data['location'],
    happening_on = data['happening_on'],
    tags = data['tags']

    new_meetup = {topic, location, happening_on, tags}
    models.Meetup.create_meetup(new_meetup)
    return jsonify({"status": 201, "message": "new meetup created successfully", "meetup": new_meetup})
# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             return ("You need to login first")
#             # return redirect(url_for('login_page'))

#     return wrap

# def admin_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'is_admin' in session:
#             return f(*args, **kwargs)
#         else:
#             return ("You are not authorized to view this page")
#             # return redirect(url_for('login_page'))

#     return wrap