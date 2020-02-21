from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(180), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    def __repr__(self):
        return f"<User:{self.name} | {self.email}>"

    def __str__(self):
        return self.name
   
    def generate_password(self,password):
        self.password = generate_password_hash(password)
        
    def check_password(self,password):
        return check_password_hash(self.password,password)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    team = db.Column(db.String, nullable=False)
    pos = db.Column(db.String, nullable=False)
    age = db.Column(db.Float, nullable=False)
    gp = db.Column(db.String, nullable=False)
    mpg = db.Column(db.Float, nullable=False)
    fta = db.Column(db.String, nullable=False)
    ftp = db.Column(db.Float, nullable=False)
    twpa = db.Column(db.String, nullable=False)
    twpp = db.Column(db.Float, nullable=False)
    thpa = db.Column(db.String, nullable=False)
    thpp = db.Column(db.Float, nullable=False)
    ppg = db.Column(db.Float, nullable=False)
    rpg = db.Column(db.Float, nullable=False)
    apg = db.Column(db.Float, nullable=False)
    spg = db.Column(db.Float, nullable=False)
    bpg = db.Column(db.Float, nullable=False)
    topg = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Record: {self.name} ({self.team}) | {self.pos}>"
    def to_dict(self):
	    data = dict(
		id=self.id,
		name=self.name,
		team=self.team,
		pos=self.pos,
		age=self.age,
		gp=self.gp,
		mpg=self.mpg,
		fta=self.fta,
		ftp=self.ftp,
		twpa=self.twpa,
		twpp=self.twpp,
		thpa=self.thpa,
		thpp=self.thpp,
		ppg=self.ppg,
		rpg=self.rpg,
		apg=self.apg,
		bpg=self.bpg,
		topg=self.topg
		)
	    return data

@login.user_loader
def get_user(id):
    return User.query.get(int(id))

