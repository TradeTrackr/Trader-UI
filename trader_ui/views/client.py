from flask import Blueprint, render_template, request
import json
from trader_ui.config import Config
from trader_ui.utilities import authentication
from trader_ui.dependencies.enquiry_api import EnquiryApi
from trader_ui.dependencies.account_api import TraderAccountApi
from trader_ui.dependencies.quotes_api import QuotesAPI

client = Blueprint('client', __name__)

@client.route("/client/enquiry/<id>")
@authentication.token_required
@authentication.check_enquiry_accounts
def enquiry(id):
    enquiry = EnquiryApi().get_enquiry_and_activity(id)
    categories = TraderAccountApi().get_categories()
    quotes = QuotesAPI().get_quotes(id)

    if enquiry != []:
        enquiry=enquiry[0]
    return render_template("pages/client/enquiry.html",
                            error="none",
                            CDN_URL=Config.CDN_URL,
                            categories=json.loads(categories),
                            quotes=quotes,
                            enquiry=enquiry
                        )


@client.route("/client/enquiries")
@authentication.token_required
def enquiries():
    enquiries = EnquiryApi().get_enquiries()

    return render_template("pages/client/enquiries.html",
                            error="none",
                            CDN_URL=Config.CDN_URL,
                            enquiries_list=enquiries
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

@client.route("/client/new_quote", methods=["POST"])
def new_quote():
    post_data = request.form
    new_quote = QuotesAPI().new_quote(post_data)
    EnquiryApi().update_enquiry_status('Quote Sent', post_data.get('enquiry_id'))

    return new_quote