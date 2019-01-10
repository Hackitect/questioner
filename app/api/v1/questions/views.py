from flask import Blueprint, request, jsonify, jsonify
import datetime
from app.api.v1.questions import models as ObjQuestions
from app.api.v1.questions.models import QuestionDB

question_class = ObjQuestions.Question()

questions = Blueprint('questions', __name__, url_prefix='/api/v1')

#post a meetup
@questions.route("/questions", methods=['POST'])
def post_question():
    data = request.get_json
    # return jsonify({"message": "route to post a question"}), 201
    
    if data:
        id = len(QuestionDB)+1
        title  = data['title']
        body = data['body']
        createdBy = data['userId']
        createdOn = datetime.datetime.now()
        meetup = 1
        votes = 0
        

        newQ = {"id": id, "title": title, "body": body, "meetup": meetup, "createdBy": createdBy, "createdOn": createdOn, "votes": votes}
        

        question_class.save(newQ)
        return jsonify({ 'status': 201, 'data': newQ, }), 201 
       
    
    else:
        return jsonify({'status':400,'error': 'you must have title, body and userId'}), 400
        
    

   