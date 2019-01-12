import unittest
from app import create_app
from flask import jsonify, json
import pytest

class TestQuestionsEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testinig = True
        self.client = self.app.test_client()

        """ mock data for testing endpoint """
        self.test_1 = {
                "id": 1,
                "createdOn": "2019, 1, 8, 7, 50, 55, 529588",
                "userId": 1, 
                "meetupId": 1,
                "title": "Andela Workshop",
                "body": "When are we meeting to discuss the creation of tests?",
                "votes": 3
                }
        self.vote = {"question_id": 1}

    
    def test_postquestion(self):
        """ Test for posting a question record. """
        response = self.client.post('/api/v1/questions', 
                                                    data =  json.dumps(self.test_1),
                                                    content_type = "application/json")
        result = json.loads(response.data.decode('utf-8')) 
        self.assertEqual(response.status_code, 201)
        self.assertIn('Andela Workshop', str(result))
    
    def test_upvote(self):
        response = self.client.patch('/api/v1/questions/1/upvote', 
        data=json.dumps(self.vote), 
        content_type = "application/json")
        self.assertEqual(response.status_code, 200)
        
    
    def test_downvote(self):
        response = self.client.patch('/api/v1/questions/1/downvote', 
        data=json.dumps(self.vote), 
        content_type = "application/json")
        self.assertEqual(response.status_code, 200)

    
if __name__ == '__main__':
    unittest.main()
        