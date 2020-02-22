from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
 

class SessionForm(FlaskForm):
    submitSession = SubmitField('CLEAR SESSION')

class PPG_MPGForm(FlaskForm):
    submit_ppg_mpgForm = SubmitField('PPG/MPG')