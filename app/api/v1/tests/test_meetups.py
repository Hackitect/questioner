import unittest
from app import create_app
from flask import jsonify, jsonify
import pytest

class TestMeetupEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testinig = True
        self.client = self.app.test_client()

        ''' This is the response spec for a meeting
        {
            "status": Integer,
            "data": [{
                "id": Integer,
                "topic": String,
                "location": String
                "happeningOn": Date,
                "tags": [String, String, ....]
            }

            ]
        }
        '''

        """ mock data for testing endpoint """
        self.test_1 = {
            "data": [{
                "id": 1,
                "topic": "Andela Hackathon",
                "location": "PAC University",
                "happeningOn": "",
                "tags": ["python", "machine learning"]
            }]
        }
    def getmeetup(self):
        """ Test for returning meeting using meeting id"""
        pass
    
    def postmeetup(self):
        """ Test for Creating an meetup record. """
        response = self.client.post('/api/v1/meetups', 
                                                    data =  json.dumps(self.test_1),
                                                    content_type = "application/json")
        result = json.loads(response.data.decode('utf-8')) 
        self.assertEqual(response.status_code, 200)
      
if __name__ == '__main__':
    unittest.main()
        