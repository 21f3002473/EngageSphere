from flask import Blueprint, render_template, redirect, url_for

sponsor_routes = Blueprint('sponsor_routes', __name__, template_folder='templates/sponsor')

@sponsor_routes.route('/', methods=['GET'])
def sponsor():
    return "sponsor route is working fine"
    # return render_template('sponsor/index.html')

@sponsor_routes.route('/dashboard', methods=['GET'])
def dashboard():
    return "sponsor dashboard is working fine"
    # campaigns = Campaign.query.all()
    # ad_requests = AdRequest.query.all()
    # return {"campaigns": campaigns, "ad_requests": ad_requests}