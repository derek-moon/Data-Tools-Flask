from flask import Flask
from flask_dotenv import DotEnv

import os
from config import Config

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_migrate import Migrate
migrate = Migrate()

from flask_login import LoginManager

login = LoginManager()
login.login_view = 'account.login'
login.login_message_category = 'danger'


basedir = os.path.dirname(os.path.abspath(__file__))

def create_app(config_class=Config):
    app = Flask(__name__)
    
   
    app.config['SQLALCHEMY_DATABASE_URI'] = os.path.join(basedir,'app.db')

    app.config.from_object(config_class)

    db.init_app(app)

    migrate.init_app(app,db)

    login.init_app(app)

    from app.blueprints.main import main
    app.register_blueprint(main, url_prefix='/')

    from flask_moment import Moment
    moment = Moment(app)
    
    with app.app_context():
        from app import models
    return app

