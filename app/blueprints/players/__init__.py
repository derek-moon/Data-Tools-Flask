from flask import Blueprint

players = Blueprint('players', __name__, template_folder='templates')

from app.blueprints.players import routes

