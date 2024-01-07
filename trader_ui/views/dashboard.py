from flask import Blueprint, render_template
import json
from trader_ui.config import Config
from trader_ui.utilities import authentication

dashboard = Blueprint('dashboard', __name__)

@dashboard.route("/home")
@authentication.token_required
def home():
    return render_template("pages/dashboard/dashboard.html", error="none", CDN_URL=Config.CDN_URL)
