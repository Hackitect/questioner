import unittest
from app import create_app
from flask import jsonify, json
import pytest

class TestMeetupEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
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
        self.test_2 = {}
    def test_getmeetup(self):
        """ Test for returning meetups """
        response = self.client.get('api/v1/meetups')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Andela Hackathon', str(result))
    
    def test_postmeetup(self):
        """ Test for Creating an meetup record. """
        response = self.client.post('/api/v1/meetups', 
                                                    data =  json.dumps(self.test_1),
                                                    content_type = "application/json")
        result = json.loads(response.data.decode('utf-8')) 
        self.assertEqual(response.status_code, 201)
        self.assertIn('Andela Hackathon', str(result))

    def test_api_get_meetup_by_id(self):
        """ Test for returning meeting using meeting id [will use id = 1] """

        postval = self.client.post('/api/v1/meetups', 
                                                    data =  json.dumps(self.test_1),
                                                    content_type = "application/json")
        self.assertEqual(postval.status_code, 200)                                           
        response = self.client.get('api/v1/meetups/1')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('The Hub', str(result))
      
if __name__ == '__main__':
    unittest.main()
        