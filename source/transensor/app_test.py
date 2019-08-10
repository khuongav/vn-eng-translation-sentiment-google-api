# pylint: disable=missing-docstring,relative-import,duplicate-code
import unittest
import json
from app import create_app
from mock import patch

class TestTransensor(unittest.TestCase):
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

    @patch('transensor.app.ApiTranslator')
    @patch('transensor.app.ApiSentiment')
    def test_transensor(self, mock_sentiment, mock_translate):
        translate = mock_translate()
        translate.translate_vi.return_value = "Bad movie"

        sentiment = mock_sentiment()
        sentiment.sentiment_en.return_value = "0"

        # It should be "Good movie" & "1" if mock fail
        data = self.send_request("Phim hay")
        self.assertEqual(data['success'], True)
        self.assertEqual(data['translate_en'], "Bad movie")
        self.assertEqual(data['sentiment_en'], "0")
