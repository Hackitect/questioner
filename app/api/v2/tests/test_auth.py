import unittest
from app import create_app
from flask import jsonify, json
import pytest, datetime

class TestAuthEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testinig = True
        self.client = self.app.test_client()
        self.date = datetime.datetime.now()

        """ mock data for testing endpoint """
        self.test_signup_data = {
                "firstname" : "Charles",
                "lastname" : "Mwangi",
                "othername" : "Njenga",
                "email" : "mwangicharles@gmail.com",
                "phoneNumber" : "0722867603",
                "username" : "cnjenga",
                "registered" : "self.date",
                "isAdmin" : 1      
                }
        self.test_signin_data = {"email": "mwangicharles@gmail.com", "password": "password123"}
        self.test_nullDATA = {}
    
    
    def test_signup(self):
        """ Test sign up in using null data. """
        response = self.client.post('/api/v2/auth/signup', 
                                                    data =  json.dumps(self.test_nullDATA),
                                                    content_type = "application/json")
        # result = json.loads(response.data.decode('utf-8')) 
        self.assertEqual(response.status_code, 400)       
    
    def test_signin(self):
        response = self.client.post('/api/v2/auth/login', 
        data=json.dumps(self.test_signin_data), 
        content_type = "application/json")
        self.assertEqual(response.status_code, 201)
    
    def test_sign_nullDATA(self):
        response = self.client.post('api/v2/auth/login',
        data=json.dumps(self.test_nullDATA),
        content_type = "application/json")
        self.assertEqual(response.status_code, 400)
        
    
       
if __name__ == '__main__':
    unittest.main()
        