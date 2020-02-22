from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SessionForm(FlaskForm):
    submitSession = SubmitField('CLEAR SESSION')
