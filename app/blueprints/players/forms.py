from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
 

class SessionForm(FlaskForm):
    submitSession = SubmitField('CLEAR SESSION')

class PPG_MPGForm(FlaskForm):
    submit_ppg_mpgForm = SubmitField('PPG/MPG')

class AGE_MPGForm(FlaskForm):
    submit_age_mpgForm = SubmitField('AGE/MPG')

class THPP_MPGForm(FlaskForm):
    submit_ttpp_mpgForm = SubmitField('3P%/MPG')