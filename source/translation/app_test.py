# pylint: disable=missing-docstring,relative-import,duplicate-code
import unittest
import json
from app import create_app
from mock import patch

class TestTranslate(unittest.TestCase):
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

    @patch('translation.app.GTranslate')
    def test_translate(self, mock_translate):
        translate = mock_translate()
        translate.vi_to_en.return_value = "for"

        # It should be "collect" if mock fail
        data = self.send_request("cho")
        self.assertEqual(data['success'], True)
        self.assertEqual(data['data'], "for")
