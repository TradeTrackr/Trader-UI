import json
import requests
from flask import current_app, g, request
from trader_ui.config import Config

class AccountApi():

    def get_account(email):
        params = {"email": email}

        headers = {
            "Content-Type": "application/json",
        }

        resp = requests.get(
            Config.ACCOUNT_API_URL + "/get_company_by_email",
            data=json.dumps(params),
            headers=headers,
        )

        return json.loads(resp.text)
