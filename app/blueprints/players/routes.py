import requests, csv, os, base64, io
from app import  db
from flask import current_app, render_template, redirect, url_for, flash, session, jsonify
from app.models import PlayerRecord
from flask_login import login_user, logout_user, login_required, current_user
from app.blueprints.players.forms import SessionForm, PPG_MPGForm

from app.blueprints.players import players
from app.blueprints.players.getData import cleanPlayerData

from bs4 import BeautifulSoup
from _datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

@players.route('/')
def player():
    sessionForm = SessionForm()
    ppg_mpgForm = PPG_MPGForm()
    #data = PlayerRecord.query.filter(PlayerRecord.mpg > 20)
    #print(f"Mean: {np.mean(ppg_list)}")
    #plt.hist(ppg_list)
    
    
    context = dict(sessionForm=sessionForm, ppg_mpgForm=ppg_mpgForm)

    return render_template('players.html', **context)


@players.route('/ppg_mpg', methods=['POST'])
def ppg_mpg():
    sessionForm = SessionForm()
    ppg_mpgForm = PPG_MPGForm()

    data = PlayerRecord.query.all()
    ppg_list = []
    mpg_list = []

    for row in data:
        ppg_list.append(row.ppg)
        mpg_list.append(row.mpg)

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("PPG vs MPG")
    axis.set_xlabel("Points Per Game")
    axis.set_ylabel("Minutes Per Game")
    axis.grid()
    axis.plot(mpg_list, ppg_list, "ro")

    

    context = dict(graph=graphHelper(fig),sessionForm=sessionForm, ppg_mpgForm=ppg_mpgForm)
    flash("Graph added","info")

    return render_template('ppg-mpg.html', **context)


@players.route('/clearSession', methods=['POST'])
def clearSession():
    session.clear()
    flash("Session has been cleared","info")
    return redirect(url_for('players.player'))

#uploads updated player data to server
@players.route('/upload')
def upload():
    session['data'] = cleanPlayerData(dataHelper())
    flash("Retrieved and Updated Database Successfully","success")
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

def graphHelper(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    graph = pngImageB64String
    return graph
