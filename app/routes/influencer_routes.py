from flask import Blueprint, render_template, redirect, url_for

influencer_routes = Blueprint('influencer_routes', __name__, template_folder='templates/influencer')

@influencer_routes.route('/', methods=['GET'])
def influencer():
    return "influencer route is working fine"
    # return render_template('influencer/index.html')

@influencer_routes.route('/dashboard', methods=['GET'])
def dashboard():
    return "influencer dashboard is working fine"
    # campaigns = Campaign.query.all()
    # ad_requests = AdRequest.query.all()
    # return {"campaigns": campaigns, "ad_requests": ad_requests}
