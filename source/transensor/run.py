# pylint: disable=missing-docstring,relative-import
from app import create_app

APP = create_app()
APP.run(host='0.0.0.0', port=80, debug=True)
