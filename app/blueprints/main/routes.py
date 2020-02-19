from app import  db
from flask import current_app, render_template, redirect, url_for, flash
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user

from app.blueprints.main import main


@main.route('/', methods=['GET','POST'])

def index():
    
    context = {
        
    }
   
    return render_template('index.html', **context)