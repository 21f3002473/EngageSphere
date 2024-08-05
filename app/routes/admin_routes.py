from flask import Blueprint, render_template, redirect , url_for
from app.models import User, Campaign, AdRequest

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/admin/dashboard', methods=['GET'])
def dashboard():

    return "admin dashboard is working fine"
    # campaigns = Campaign.query.all()
    # ad_requests = AdRequest.query.all()
    # return {"campaigns": campaigns, "ad_requests": ad_requests}