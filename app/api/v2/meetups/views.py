from flask import Blueprint, request, jsonify, session

meetups = Blueprint('meetups', __name__, url_prefix='/api/v2')

#route to delete a meetup using meetup id
@meetups.route("/meetups/<int:meetup_id>", methods=['DELETE'])
# @admin_required
def delete():
    pass

@meetups.route("/meetups/", methods=['POST'])
def create_meetup():
    data = request.get_json()
    if not data or not data['topic'] or not data['location'] or not data['happening_on']:
        return jsonify({"status": 400, "message": "missing some field"})
        meetup_data = Meetup(
            data['topic'],
            data['location'],
            data['happening_on'],
            data['tags']
        )
        new_meetup = meetup_data.create_meetup()
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