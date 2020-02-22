import requests, csv, os, base64, io
from app import  db
from flask import current_app, render_template, redirect, url_for, flash, session, jsonify
from app.models import PlayerRecord
from app.blueprints.api import api


@api.route('/players', methods=['GET'])
def get_records():
    data = [i.to_dict() for i in PlayerRecord.query.all()]
    return jsonify(data)
