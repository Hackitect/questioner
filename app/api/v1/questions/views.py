from flask import Blueprint, request, jsonify, jsonify
import datetime
from app.api.v1.questions import models as ObjQuestions
from app.api.v1.questions.models import QuestionDB

question_class = ObjQuestions.Question()

questions = Blueprint('questions', __name__, url_prefix='/api/v1')

def vote(question_id, status):
    data = request.get_json()
    id = data['question_id']
    params = 0
    # msg = ""
    if data:
        if status == "upvote":
            params = 1
            
        elif status == "downvote":
            params = -1
                
        for que in QuestionDB:
            if que['id'] == id:
                que['votes'] == que['votes'] + params
                return True
    else:
        return jsonify({'status':400,'error': 'you must have a questionId'}), 400

#upvote a question
@questions.route("/questions/<int:question_id>/upvote", methods=['PATCH'])
def upvote(question_id):
    vote(question_id, downvote)
    return jsonify({"status": 201, "message": "you have upvoted this question"}), 201

# route to downvote a question
# the route Downvote (decrease votes by 1) a specific question.
@questions.route("/questions/<int:question_id>/downvote", methods=['PATCH'])

def downvote(question_id):
    vote(question_id, upvote)
    return jsonify({"status": 201, "message": "you have downvoted this question"}), 201

#post a meetup
@questions.route("/questions", methods=['POST'])
def post_question():
    data = request.get_json()
    # return jsonify({"message": "route to post a question"}), 201
    id = len(QuestionDB)+1
    title  = data['title']
    body = data['body']
    createdBy = data['userId']
    createdOn = datetime.date.now()
    meetup = data['meetupId']
    votes = 0
    if data:  
        newQ = {"id": id, "title": title, "body": body, "meetup": meetup, "createdBy": createdBy, "createdOn": createdOn, "votes": votes}
        question_class.save(newQ)
        return jsonify({ 'status': 201, 'data': newQ, }), 201 
       
    
    else:
        return jsonify({'status':400,'error': 'you must have title, body and userId'}), 400
        
    

   