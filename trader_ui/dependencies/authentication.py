import requests
import json

class AuthenticationService:
    def __init__(self, config):
        self.config = config

    def verify_login(self, email, password):
        url = f"{self.config.LOGIN_API_URL}/verify_login"
        payload = {"email": email.lower(), "password": password}
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        return response

    def reset_password(self, email, code, new_password):
        # Implement password reset logic here
        pass

    def get_company_account(self, id):
        resp = requests.get(self.config.USERS_API_URL + "/comp/" + str(id))
        data = json.loads(resp.text)
        return data

    def get_account(self, email):
        params = {"email": email}

        headers = {
            "Content-Type": "application/json",
        }

        resp = requests.get(
            self.config.USERS_API_URL + "/get_company_by_email",
            data=json.dumps(params),
            headers=headers,
        )

        data = json.loads(resp.text)
        return data
