from flask import Blueprint, render_template, request
import json
from trader_ui.config import Config
from trader_ui.utilities import authentication
from trader_ui.dependencies.enquiry_api import EnquiryApi
from trader_ui.dependencies.quotes_api import QuotesAPI
from trader_ui.dependencies.account_api import TraderAccountApi

dashboard = Blueprint('dashboard', __name__)

@dashboard.route("/home")
@authentication.token_required
def home():
    enquiries = EnquiryApi().get_new_enquiries()

    return render_template("pages/dashboard/dashboard.html",
                            error="none",
                            CDN_URL=Config.CDN_URL,
                            enquiries_list=enquiries
                        )

@dashboard.route("/dashboard/get_quotes")
@authentication.token_required
def get_quotes():
    calendar_quotes = QuotesAPI().get_company_calendar_quotes()
    return calendar_quotes


@dashboard.route("/dashboard/new_event", methods=["POST"])
def new_event():
    post_data = request.form
    new_quote = QuotesAPI().new_event(post_data)

    return new_quote


@dashboard.route("/dashboard/update_event/<id>", methods=["POST"])
def update_event(id):
    post_data = request.form
    print(post_data)
    new_quote = QuotesAPI().update_event(post_data, id)

    return new_quote


@dashboard.route("/dashboard/get_categories")
@authentication.token_required
def get_categories():
    categories = TraderAccountApi().get_categories()
    return categories