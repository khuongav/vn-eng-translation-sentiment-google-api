# pylint: disable=missing-docstring,too-few-public-methods,global-statement,no-self-use,relative-import,no-member
from flask import Flask, Blueprint, jsonify, request
import constants as const
import requests

# This class using API sentiment micro-service
class ApiSentiment(object):
    def __init__(self):
        pass

    def sentiment_en(self, text):
        """Call API sentiment in the text."""
        response = requests.post(const.URL_SENTIMENT_SERVICE, json={"txt":text})
        return response.text


# This class using API translator micro-service
class ApiTranslator(object):
    def __init__(self):
        pass

    def translate_vi(self, text):
        """Call API translator in the text."""
        response = requests.post(const.URL_TRANSLATOR_SERVICE, json={"txt":text})
        return response.text

# Our flask server begin here
BLUEPRINT = Blueprint('transensor', __name__)
API_TRANS = None
API_SEN = None

@BLUEPRINT.route("/", methods=['POST'])
def transensor():
    global API_TRANS, API_SEN
    if API_TRANS is None:
        API_TRANS = ApiTranslator()
    if API_SEN is None:
        API_SEN = ApiSentiment()
    text = request.get_json()['txt']

    translated_en = API_TRANS.translate_vi(text)
    sentiment_en = API_SEN.sentiment_en(translated_en)
    rest_json = {"success": True, "translate_en": translated_en, "sentiment_en": sentiment_en}

    return jsonify(rest_json)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(BLUEPRINT)

    return app
