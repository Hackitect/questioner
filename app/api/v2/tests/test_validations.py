import unittest
from app import create_app
from app.api.v2.utils import validators

class TestsforValidations(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.username1 = 'x'

def test_password(self, Validators):
    self.assertEqual(is_valid_email('2222'), False)

