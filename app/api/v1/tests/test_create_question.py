import unittest
from app import create_app
from flask import jsonify, json
import pytest

class TestMeetupEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testinig = True
        self.client = self.app.test_client()

        """ mock data for testing endpoint """
        self.test_1 = {
            "data": [{
                "id": 1,
                "createdOn": "2019, 1, 8, 7, 50, 55, 529588",
                "createdBy": 1, # represents the user asking the question
                "meetup": 1, # represents the meetup the question is for
                "title": "Andela Workshop",
                "body": "When are we meeting to discuss the creation of tests?",
                "votes": 3
                }]
        }

    
    def postquestion(self):
        """ Test for posting a question record. """
        response = self.client.post('/api/v1/question', 
                                                    data =  json.dumps(self.test_1),
                                                    content_type = "application/json")
        result = json.loads(response.data.decode('utf-8')) 
        self.assertEqual(response.status_code, 201)
        self.assertIn('Andela Workshop', str(result))

    
if __name__ == '__main__':
    unittest.main()
        