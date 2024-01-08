from flask import Blueprint, render_template, session
import json
from trader_ui.config import Config
from trader_ui.utilities import authentication
from trader_ui.dependencies.enquiry_api import EnquiryApi

dashboard = Blueprint('dashboard', __name__)

@dashboard.route("/home")
@authentication.token_required
def home():
    print(session['id'])
    enquiries = EnquiryApi().get_enquiries()
    print(enquiries)

    return render_template("pages/dashboard/dashboard.html",
                            error="none",
                            CDN_URL=Config.CDN_URL,
                            enquiries_list=enquiries
                        )
