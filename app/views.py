# this files combines all the views of the app

from flask import Blueprint, render_template, redirect , url_for
from app.models import User, Campaign, AdRequest
from app.routes.sponsor_routes import sponsor_routes
from app.routes.admin_routes import admin_routes
from app.routes.influencer_routes import influencer_routes

class AllViews:
    def __init__(self, app):
        self.app = app
        self.__register_routes()

    def __register_routes(self):
        self.app.register_blueprint(admin_routes, url_prefix='/admin')
        self.app.register_blueprint(sponsor_routes, url_prefix='/sponsor')
        self.app.register_blueprint(influencer_routes, url_prefix='/influencer')
