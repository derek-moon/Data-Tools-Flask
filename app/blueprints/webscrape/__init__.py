from flask import Blueprint

webscrape = Blueprint('webscrape', __name__, template_folder='templates')

from app.blueprints.webscrape import routes

def getData(data):
    data_list = []
    for tr in data:
        data_values = []

        for dIndex, dValue in enumerate(tr):
            print(dIndex,dValue)