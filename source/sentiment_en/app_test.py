# pylint: disable=missing-docstring,relative-import,duplicate-code
import unittest
import json
from app import create_app
from mock import patch

class TestSentiment(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def send_request(self, txt):
        rq_data = '{"txt": "'+txt+'"}'
        send_data = self.client.post(
            '/',
            data=rq_data,
            headers={'Content-Type' : 'application/json'}
        )

        return json.loads(send_data.get_data(as_text=True))

    @patch('sentiment_en.app.GSentiment')
    def test_sentiment(self, mock_sentiment):
        sentiment = mock_sentiment()
        sentiment.sentiment_en.return_value = '0'

        # It should be "1" if mock fail
        data = self.send_request("This movie is really good")
        self.assertEqual(data['success'], True)
        self.assertEqual(data['data'], "0")
