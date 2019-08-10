# pylint: disable=missing-docstring,too-few-public-methods,global-statement,no-self-use,relative-import
import six
from flask import Flask, Blueprint, jsonify, request
from google.cloud import language # pylint: disable=import-error,no-name-in-module
from google.cloud.language import enums # pylint: disable=import-error,no-name-in-module
from google.cloud.language import types # pylint: disable=import-error,no-name-in-module

# This class using google cloud sentiment service
class GSentiment(object):
    def __init__(self):
        self.client = language.LanguageServiceClient()

    def sentiment_en(self, text):
        """Detects sentiment in the text."""
        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')

        # Instantiates a plain text document.
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects sentiment in the document. You can also analyze HTML with:
        #   document.type == enums.Document.Type.HTML
        sentiment = self.client.analyze_sentiment(document).document_sentiment

        return 0 if (sentiment.score < 0) else 1

# Our flask server begin here
BLUEPRINT = Blueprint('sentiment', __name__)
GSEN = None

@BLUEPRINT.route("/", methods=['POST'])
def sentiment_service():
    global GSEN
    if GSEN is None:
        GSEN = GSentiment()

    text = request.get_json()['txt']
    rest_json = {"success": True, "data": GSEN.sentiment_en(text)}

    return jsonify(rest_json)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(BLUEPRINT)

    return app
