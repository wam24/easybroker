import unittest
import requests
from main import PropertyCLI


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.token = 'l7u502p8v46ba3ppgvj5y2aad50lb9'
        self.url = "https://api.stagingeb.com/v1/properties"
        self.headers = {
            "accept": "application/json",
            "X-Authorization": self.token
        }

    def test_api_response(self):
        response = requests.get(self.url, headers=self.headers)

        self.assertEqual(response.status_code, 200)
        self.assertIn('content', response.json())

if __name__ == '__main__':
    unittest.main()
