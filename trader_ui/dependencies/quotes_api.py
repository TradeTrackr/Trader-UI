import json
import requests
from flask import session
from trader_ui.config import Config

class QuotesAPI():

    def get_quotes(self, id):

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {session['access_token']}"
        }

        resp = requests.get(
            Config.QUOTES_API_ENDPOINT + f"/quote/get_quotes/{id}",
            headers=headers,
        )

        return json.loads(resp.text)

    def new_quote(self, params):

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {session['access_token']}"
        }
        params = dict(params)
        params['status'] = 'new'
        
        if params.get('category_id'):
            params['category_id'] = int(params['category_id'])

        resp = requests.post(
            Config.QUOTES_API_ENDPOINT + "/quote/new",
            data=json.dumps(params),
            headers=headers,
        )
        return resp.text
