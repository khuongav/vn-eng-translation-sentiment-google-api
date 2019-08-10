# pylint: disable=missing-docstring,too-few-public-methods,global-statement,no-self-use
from flask import Flask, Blueprint, jsonify, request
from googletrans import Translator # pylint: disable=import-error,no-name-in-module

class GTranslate(object):
    def __init__(self):
        self.translator = Translator()

    def vi_to_en(self, in_text):
        return self.translator.translate(in_text).text

# Our flask server begin here
BLUEPRINT = Blueprint('translate', __name__)
GTRANS = None

@BLUEPRINT.route("/", methods=['POST'])
def translate_service():
    global GTRANS
    if GTRANS is None:
        GTRANS = GTranslate()

    text = request.get_json()['txt']
    rest_json = {"success": True, "data": GTRANS.vi_to_en(text)}

    return jsonify(rest_json)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(BLUEPRINT)

    return app
