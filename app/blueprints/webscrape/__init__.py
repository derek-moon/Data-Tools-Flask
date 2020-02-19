from flask import Blueprint

webscrape = Blueprint('webscrape', __name__, template_folder='templates')

from app.blueprints.webscrape import routes

