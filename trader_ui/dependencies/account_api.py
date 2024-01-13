import json
import requests
from flask import session
from trader_ui.config import Config

class TraderAccountApi():

    def get_account(self):
        params = {"id": id}

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {session['access_token']}"
        }

        resp = requests.get(
            Config.ACCOUNT_API_ENDPOINT + "/trader/get_company_by_email",
            data=json.dumps(params),
            headers=headers,
        )

        return json.loads(resp.text)
