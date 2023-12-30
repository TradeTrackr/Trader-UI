from flask import request, Blueprint, Response, jsonify, current_app, render_template
from trader_ui import app, config
import json

general = Blueprint('general', __name__)


@general.route("/health")
def check_status():
    return Response(response=json.dumps({
        "app": current_app.config["APP_NAME"],
        "status": "OK",
        "headers": request.headers.to_list()
    }),  mimetype='application/json', status=200)


@general.route("/showcase")
def showcase_temp():
    return "this is a test route for the plymouth university showcase"
