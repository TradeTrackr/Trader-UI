import json
import requests
from flask import current_app, g, request
from trader_ui.config import Config

class AccountApi():

    def get_account(self):
        params = {"id": id}

        headers = {
            "Content-Type": "application/json",
        }

        resp = requests.get(
            Config.ACCOUNT_API_ENDPOINT + "/get_company_by_email",
            data=json.dumps(params),
            headers=headers,
        )

        return json.loads(resp.text)
