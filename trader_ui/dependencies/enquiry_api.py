import json
import requests
from flask import current_app, g, request, session
from trader_ui.config import Config

class EnquiryApi():

    def get_enquiries(self):

        headers = {
            "Content-Type": "application/json",
        }

        resp = requests.get(
            Config.ENQUIRY_API_ENDPOINT + f"/get_enquirys/{session['id']}",
            headers=headers,
        )

        return json.loads(resp.text)

    def get_enquiry(self, id):

        headers = {
            "Content-Type": "application/json",
        }

        resp = requests.get(
            Config.ENQUIRY_API_ENDPOINT + f"/get_enquiry/{id}/{session['id']}",
            headers=headers,
        )

        return json.loads(resp.text)

    def get_enquiry_and_activity(self, id):

        headers = {
            "Content-Type": "application/json",
        }

        resp = requests.get(
            Config.ENQUIRY_API_ENDPOINT + f"/get_enquiry/{id}/{session['id']}",
            headers=headers,
        )

        return json.loads(resp.text)