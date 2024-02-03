# myapp/tests.py
import json
import requests  # Import the 'requests' library
from django.test import TestCase, Client
from django.urls import reverse

class APITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_predict_view(self):
        # Define test data
        test_data = {
            'image_url': 'https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcQifP_nk4LaZcJayOyIkx8keZOnNfN-ClbbEx-8Be06UUqNL1iNGz3Ldx8ilBw_pRAJ',
            'text': 'What is this image about?'
        }

        # Send a POST request to the predict endpoint
        response = self.client.post(reverse('predict'), data=test_data)

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response
        response_data = json.loads(response.content)

        # Check the response content
        self.assertIn('predicted_answer', response_data)

    def test_predict_end_to_end(self):
        # Define test data
        test_data = {
            'image_url': 'https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcQifP_nk4LaZcJayOyIkx8keZOnNfN-ClbbEx-8Be06UUqNL1iNGz3Ldx8ilBw_pRAJ',
            'text': 'What is this image about?'
        }

        # Send a POST request to the API endpoint
        response = requests.post('http://localhost:8000/api/predict/', data=test_data)

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response
        response_data = response.json()

        # Check the response content
        self.assertIn('predicted_answer', response_data)
