import json
import requests
from flask import current_app, g, request
from trader_ui.config import Config

class LoginApi():

    def update_password(payload):
        current_app.logger.info("updating password")

        url = Config.LOGIN_API_URL + "/update_pass"
        headers = {"Content-type": "application/json", "Accept": "text/plain"}

        response = g.requests.request(
            "POST", url, data=json.dumps(payload), headers=headers
        )
        return json.loads(response.text)  

    def verify_login(payload):
        current_app.logger.info("validating login")

        url = Config.LOGIN_API_URL + "/verify_login"
        headers = {"Content-type": "application/json", "Accept": "text/plain"}

        response = g.requests.request(
            "POST", url, data=json.dumps(payload), headers=headers
        )

        return json.loads(response.text)

    def reset_pass(payload):

        url = Config.LOGIN_API_URL + "/reset_pass"
        headers = {"Content-type": "application/json", "Accept": "text/plain"}

        response = g.requests.request(
            "POST", url, data=json.dumps(payload), headers=headers
        )

        return json.loads(response.text)
