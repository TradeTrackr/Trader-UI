from flask import Blueprint, render_template, jsonify
import json
from trader_ui.config import Config
from trader_ui.utilities import authentication
from trader_ui.dependencies.enquiry_api import EnquiryApi

client = Blueprint('client', __name__)

@client.route("/client/enquiry/<id>")
@authentication.token_required
@authentication.check_enquiry_accounts
def enquiry(id):
    enquiry = EnquiryApi().get_enquiry_and_activity(id)

    return render_template("pages/client/enquiry.html",
                            error="none",
                            CDN_URL=Config.CDN_URL,
                            enquiry=enquiry[0]
                        )
