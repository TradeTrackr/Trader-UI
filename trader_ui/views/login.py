from flask import (
    redirect,
    Blueprint,
    render_template,
    request,
    current_app,
    session,
    g,
)
import requests
import json
from trader_ui.exceptions import ApplicationError
from trader_ui.config import Config
from urllib.parse import urljoin
from dependencies.authentication import AuthenticationService
from dependencies.login_api import LoginApi
from dependencies.account_api import AccountApi

login = Blueprint("login", __name__)

# Routes definition
@login.route("/login")
def login_page():
    return LoginManager.display_login_page()

@login.route("/login/validate_login", methods=["POST"])
def login_validate():
    return LoginManager.validate_login()

@login.route("/login/new_pass/<email>/<random>", methods=["GET", "POST"])
def new_pass(email, random):
    if request.method == "GET":
        return render_template("pages/new_pass.html",
                email=email.lower(),
                random=random,
                CDN_URL=Config.CDN_URL
        )
                
    elif request.method == "POST":
        return LoginManager.set_new_pass(email.lower(), random)


@login.route("/login/reset_pass", methods=["GET", "POST"])
def reset_pass():
    if request.method == "GET":
        return render_template("pages/reset_pass.html", CDN_URL=Config.CDN_URL)
    elif request.method == "POST":
        return LoginManager.reset_pass_post()


class LoginManager:

    @staticmethod
    def display_login_page():
        session["next"] = request.args.get("next", "/")
        if session.get("keep_me_logged_in_company") == "logged_in":
            return redirect("./home")
        return render_template("pages/display_logins.html", error="none", CDN_URL=Config.CDN_URL)

    @staticmethod
    def validate_login():
        post_data = request.form

        payload = {}
        payload["email"] = post_data.get("email").lower()
        payload["password"] = post_data.get("password")

        json_data = LoginApi().verify_login(payload)

        get_account_by_email = AccountApi().get_account(post_data.get("email").lower())

        # code u001 has been specified to be an incorrect email and password combination so we should check for this
        if json_data["error_code"] == "u001":
            return render_template(
                "pages/display_logins.html",
                error="error-password-username",
                CDN_URL=Config.CDN_URL,
            )

        if "keep_me_logged_in" in post_data:
            if post_data["keep_me_logged_in"] == "true":
                session["keep_me_logged_in_company"] = "logged_in"
                session.permanent = True

        session["account_id"] = get_account_by_email[0]["account_id"]
        session["email"] = post_data.get("email").lower()
        session["cookie_policy"] = "yes"
        session["error"] = ""

        return redirect("./home")

    @staticmethod
    def set_new_pass(email, random):

        if random == " ":
            return render_template(
                "pages/new_pass.html",
                error="invalid-link",
                CDN_URL=Config.CDN_URL,
            )

        payload = {}
        payload["password"] = request.form["password"]
        payload["email"] = email.lower()
        payload["code"] = random
        
        json_data = LoginApi().update_password(payload)

        # code u001 has been specified to be an incorrect email and password combination so we should check for this
        if json_data["error_code"] == "u001":
            return render_template(
                "pages/new_pass.html",
                error="pass-not-set",
                CDN_URL=Config.CDN_URL,
            )
        if json_data["error_code"] == "u005":
            return render_template(
                "pages/new_pass.html",
                error="expired",
                CDN_URL=Config.CDN_URL,
            )
        if json_data["error_code"] == "u005":
            return render_template(
                "pages/new_pass.html",
                error="invalid-link",
                CDN_URL=Config.CDN_URL,
            )
        if json_data['error_code'] == 'u004':
            return render_template('pages/new_pass.html', error="expired",  CDN_URL=Config.CDN_URL)

        return render_template("pages/display_logins.html", error="mew-pass-set")

    @staticmethod
    def reset_pass_post():

        payload = {}
        payload["email"] = request.form["email"].lower()
        payload["type"] = "reset_pass_email"

        json_data = LoginApi().reset_pass(payload)

        # code u001 has been specified to be an incorrect email and password combination so we should check for this
        if json_data["error_code"] == "u001":
            return render_template(
                "pages/reset_pass.html",
                error="reset-pass-not-sent",
                CDN_URL=Config.CDN_URL,
            )

        return render_template(
            "pages/display_logins.html", error="reset-pass-sent", CDN_URL=Config.CDN_URL
        )
