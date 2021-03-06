import unittest
from app import create_app
from flask import jsonify, json
import pytest

class TestMeetupEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        

        """ mock data for testing endpoint """
        
        self.test_2 = {"topic": "Andela Hackathon","location": "PAC University", 
                        "happeningOn": "","tags": ["python", "machine learning"]}
        self.test_rsvp = {"meetup_id": 1, "topic": "Python", "status": "Yes"}
        self.rsvp_empty = []
    
    def test_getmeetup(self):
        """ Test for returning meetups """
        response = self.client.get('/api/v1/meetups')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Andela Hackathon', str(result))
    
    def test_postmeetup(self):
        """ Test for Creating an meetup record. """
        response = self.client.post('/api/v1/meetups', 
                                                    data =  json.dumps(self.test_2),
                                                    content_type = "application/json")
        result = json.loads(response.data.decode('utf-8')) 
        self.assertEqual(response.status_code, 201)
        self.assertIn('Andela Hackathon', str(result))

    def test_api_get_meetup_by_id(self):
        """ Test for returning meeting using meeting id [will use id = 1] """
        # self.assertEqual(postval.status_code, 200)                                           
        response = self.client.get('/api/v1/meetups/1')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('The Hub', str(result))
    
    def test_api_rsvp_meeting(self):
        """ test for RSVP meeting """
        response = self.client.post('/meetups/1/rsvps', 
        data = json.dumps(self.rsvp_empty), 
        content_type = "application/json")
        # result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404)
        # self.assertIn("Python", str(result))
    
       
    def test_api_meetups_upcoming(self):
        response = self.client.get('/api/v1/meetups/upcoming/')
        self.assertEqual(response.status_code, 200)
    
    def test_get_all(self):
        response = self.client.get('/api/v1/meetups')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()  