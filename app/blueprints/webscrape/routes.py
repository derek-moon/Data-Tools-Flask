import requests, csv, os
from app import  db
from flask import current_app, render_template, redirect, url_for, flash, session, jsonify
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user
from app.blueprints.webscrape.forms import CSVForm, DataPlayerForm, DataTeamForm, SessionForm, CSVForm, CronjobForm

from app.blueprints.webscrape import webscrape
from app.blueprints.webscrape.getData import  cleanPlayerData, cleanTeamData

from bs4 import BeautifulSoup



from app.blueprints.webscrape import selenium

@webscrape.route('/', methods=['GET','POST'])
def webscraper():
    dataPlayerForm = DataPlayerForm()
    dataTeamForm = DataTeamForm()
    sessionForm = SessionForm()
    csvForm = CSVForm()
    cronjobForm = CronjobForm()
    data = session.get('data')
    context = dict(data=data, dataPlayerForm=dataPlayerForm, dataTeamForm=dataTeamForm, sessionForm=sessionForm, csvForm=csvForm, cronjobForm=cronjobForm)

    return render_template('webscraper.html', **context)

@webscrape.route('/nbaPlayerData', methods=['POST'])
def nbaPlayerData():
    dataPlayerForm = DataPlayerForm()
    if dataPlayerForm.validate_on_submit():
        session['data'] = cleanPlayerData(dataHelper(), dataPlayerForm.search.data)
        flash("Retrieved Data Player Successfully","success")
        return redirect(url_for('webscrape.webscraper'))


@webscrape.route('/nbaTeamData', methods=['POST'])
def nbaTeamData():
    dataTeamForm = DataTeamForm()
    if dataTeamForm.validate_on_submit():
        session['data'] = cleanTeamData(dataHelper(), dataTeamForm.search.data)
        flash("Retrieved Team Data Successfully","success")
        return redirect(url_for('webscrape.webscraper'))

@webscrape.route('/toCSV', methods=['POST'])
def toCSV():
  column_list = ["NAME", "TEAM", "POS", "AGE", "GP", "MPG", "FTA", "FT%", "2PA", "2P%", "3PA", "3P%", "PPG", "RPG", "APG", "SPG", "BPG", "TOPG"]
  csv_list = []
  csv_list.append(column_list)

  for i in session.get('data'):
    csv_list.append(i)
  with open(os.path.join(os.path.dirname(__name__), 'data.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_list)
  flash("Information saved to CSV", "success")
  return redirect(url_for('webscrape.webscraper'))


@webscrape.route('/setCronjob',methods=['POST'])
def setCronjob():
    selenium.execute()
    flash("Cronjob is set")
    return redirect(url_for('webscrape.webscraper'))

@webscrape.route('/clearSession', methods=['POST'])
def clearSession():
    session.clear()
    flash("Session has been cleared","info")
    return redirect(url_for('webscrape.webscraper'))

def dataHelper():
    page = requests.get('https://www.nbastuffer.com/2019-2020-nba-player-stats/')
    soup = BeautifulSoup(page.content, 'html.parser')
    html = [i for i in list(soup.children)][3] 
    tr_list = html.find_all('tr')[1:]
    return tr_list