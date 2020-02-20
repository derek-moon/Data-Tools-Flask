from app import  db
from flask import current_app, render_template, redirect, url_for, flash, session
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user
from app.blueprints.webscrape.forms import DataForm, SessionForm, CSVForm, CronjobForm
from app.blueprints.webscrape import webscrape
from app.blueprints.webscrape.getData import getData, cleanData

from bs4 import BeautifulSoup
import requests


from app.blueprints.webscrape import selenium

@webscrape.route('/setCronjob',methods=['POST'])
def setCronjob():
    selenium.execute()
    flash("Cronjob is set")
    return redirect(url_for('webscrape.webscraper'))


@webscrape.route('/', methods=['GET','POST'])
def webscraper():
    dataForm = DataForm()
    sessionForm = SessionForm()
    csvForm = CSVForm()
    cronjobForm = CronjobForm()
    data = session.get('data')
    context = dict(data=data, dataForm=dataForm, sessionForm=sessionForm, csvForm=csvForm, cronjobForm=cronjobForm)

    context = dict(
       data=data, dataForm=dataForm, sessionForm=sessionForm, csvForm=csvForm, cronjobForm=cronjobForm
    )
   
    return render_template('webscraper.html', **context)
#38

@webscrape.route('/nbaData', methods=['POST'])
def nbaData():
    dataForm = DataForm()
    if dataForm.validate_on_submit():
        page = requests.get('https://www.nbastuffer.com/2019-2020-nba-player-stats/')
        soup = BeautifulSoup(page.content, 'html.parser')
        html = [i for i in list(soup.children)][3] 
        tr_list = html.find_all('tr')[1:]
        session['data'] = cleanData(tr_list, dataForm.search.data)
        print(session.get('data'))
        flash("Retrieved Data Successfully","success")
        return redirect(url_for('webscrape.webscraper'))

