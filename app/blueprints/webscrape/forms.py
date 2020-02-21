from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class DataPlayerForm(FlaskForm):
    search = StringField()
    submitPlayerData = SubmitField('Scrape Data')

class DataTeamForm(FlaskForm):
    search = StringField()
    submitTeamData = SubmitField('Scrape Data')

class SessionForm(FlaskForm):
    submitSession = SubmitField('CLEAR SESSION')

class CSVForm(FlaskForm):
    submitCSV = SubmitField('Save to CSV')
    
class CronjobForm(FlaskForm):
    submitCronJob = SubmitField("SET CRONJOB")