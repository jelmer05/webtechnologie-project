from webtech import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin) :

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    boekingen_id = db.relationship('Boeking', backref='user', uselist=False) 

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Boeking(db.Model):
    __tablename__ = 'boekingen'
    id = db.Column(db.Integer, primary_key =True)
    gast_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    huis_id = db.Column(db.Integer, db.ForeignKey('huisjes.id'))
    weeknummer = db.Column(db.Integer, index = True)
    
    def __init__(self, gast_id, huis_id, weeknummer) -> None:
        self.gast_id = gast_id
        self.huis_id = huis_id
        self.weeknummer = weeknummer
        
    

class Huisje(db.Model):

    __tablename__ = 'huisjes'
    id = db.Column(db.Integer, primary_key = True)
    personen = db.Column(db.Integer, index = True)
    weekprijs = db.Column(db.Float, index=True)
    beschrijving = db.Column(db.Text)
    afbeelding = db.Column(db.Text)
    boeking_id = db.relationship('Boeking', backref='huis')

    def __init__(self,  personen, weekprijs, beschrijving,afbeelding) -> None:
        self.personen = personen
        self.weekprijs = weekprijs
        self.beschrijving = beschrijving
        self.afbeelding = afbeelding

        


