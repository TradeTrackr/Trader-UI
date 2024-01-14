from flask import Blueprint, render_template
import json
from trader_ui.config import Config
from trader_ui.utilities import authentication
from trader_ui.dependencies.enquiry_api import EnquiryApi
from trader_ui.dependencies.account_api import TraderAccountApi

client = Blueprint('client', __name__)

@client.route("/client/enquiry/<id>")
@authentication.token_required
@authentication.check_enquiry_accounts
def enquiry(id):
    enquiry = EnquiryApi().get_enquiry_and_activity(id)
    categories = TraderAccountApi().get_categories()
    print(categories)
    return render_template("pages/client/enquiry.html",
                            error="none",
                            CDN_URL=Config.CDN_URL,
                            categories=categories,
                            enquiry=enquiry[0]
                        )


@client.route("/user/profile/<email>")
@authentication.token_required
@authentication.check_enquiry_accounts
def user_profile(email):
    enquiry = EnquiryApi().get_user_properties_and_history(email)
    return render_template("pages/client/user.html",
                            error="none",
                            CDN_URL=Config.CDN_URL,
                            email=email,
                            enquiry=enquiry
                        )