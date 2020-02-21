import requests, csv, os
from app import  db
from flask import current_app, render_template, redirect, url_for, flash, session, jsonify
from app.models import PlayerRecord
from flask_login import login_user, logout_user, login_required, current_user

from app.blueprints.players import players
from app.blueprints.players.getData import cleanPlayerData

from bs4 import BeautifulSoup
from _datetime import datetime

@players.route('/')
def player():
    context = {

    }

    pass
    return render_template('players.html', **context)


#uploads updated player data to server
@players.route('/upload')
def upload():
    session['data'] = cleanPlayerData(dataHelper())
    flash("Retrieved Team Data Successfully","success")
    data = session.get('data')

    column_list = ["NAME", "TEAM", "POS", "AGE", "GP", "MPG", "FTA", "FT%", "2PA", "2P%", "3PA", "3P%", "PPG", "RPG", "APG", "SPG", "BPG", "TOPG"]
    db_list = []
    db_list.append(column_list)


    for inner_list in session.get('data'):
        db_list.append(inner_list)
        record = PlayerRecord(
        name=inner_list[0],
        team=inner_list[1],
        pos=inner_list[2],
        age=inner_list[3],
        gp=inner_list[4],
        mpg=inner_list[5],
        fta=inner_list[6],
        ftp=inner_list[7],
        twpa=inner_list[8],
        twpp=inner_list[9],
        thpa=inner_list[10],
        thpp=inner_list[11],
        ppg=inner_list[12],
        rpg=inner_list[13],
        apg=inner_list[14],
        spg=inner_list[15],
        bpg=inner_list[16],
        topg=inner_list[17]
      )
        db.session.add(record)
        db.session.commit()

    context = dict(data=data)
    return render_template('players.html', **context)



def dataHelper():
    page = requests.get('https://www.nbastuffer.com/2019-2020-nba-player-stats/')
    soup = BeautifulSoup(page.content, 'html.parser')
    html = [i for i in list(soup.children)][3] 
    tr_list = html.find_all('tr')[1:]
    return tr_list