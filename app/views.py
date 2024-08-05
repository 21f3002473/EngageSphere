import routes.admin_routes as admin_routes
from . import app
app.register_blueprint(admin_routes, url_prefix='/admin')


