from flask import Blueprint, render_template, redirect, url_for
from app.models import User, Campaign, AdRequest

admin_routes = Blueprint( 'admin_routes', __name__, template_folder='templates/admin' )


@admin_routes.route('/', methods=['GET'], )
def admin():
    return "admin route is working fine"
    # return render_template('admin/index.html')

@admin_routes.route('/dashboard', methods=['GET'])
def dashboard():
    return "admin dashboard is working fine"
    # campaigns = Campaign.query.all()
    # ad_requests = AdRequest.query.all()
    # return {"campaigns": campaigns, "ad_requests": ad_requests}
