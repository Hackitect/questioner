import datetime

QuestionDB = [
    {
        "id": 1,
        "createdOn": "2019, 1, 8, 7, 50, 55, 529588",
        "createdBy": 1, # represents the user asking the question
        "meetup": 1, # represents the meetup the question is for
        "title": "Andela Workshop",
        "body": "When are we meeting to discuss the creation of tests?",
        "votes": 3
    }
]

class Question:
    def save(self, newQ):
        QuestionDB.append(self)
    
    def upvote(self):
        pass
