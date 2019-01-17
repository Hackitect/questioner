import unittest
from app.api.v1.utils.validators import Validators

class TestsforValidations(unittest.TestCase, Validators):

    def test_password(self):
        self.assertEqual(self.is_valid_password('2222'), False)
        self.assertEqual(self.is_valid_password('youathere'), False)
        self.assertEqual(self.is_valid_password('Password123!'), True)
    
    def Test_email(self):
        self.assertEqual(self.is_valid_email('x'), False)
        self.assertEqual(self.is_valid_email(123), False)
        self.assertEqual(self.is_valid_email('mwangicharles@gmail.com'), True)
        self.assertEqual(self.is_valid_email('the beast'), False)
    
    def test_username(self):
        self.assertEqual(self.is_valid_username('MO'), False)
        self.assertEqual(self.is_valid_username('MO001'), True)
        self.assertEqual(self.is_valid_username('cnjenga'), True)



if __name__ == '__main__':
    unittest.main()