from flask import Blueprint

api = Blueprint('api', __name__, template_folder='templates')

from app.blueprints.api import routes

