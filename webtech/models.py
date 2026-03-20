from webtech import db
class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    naam= db.Column(db.Text)

    def __init__(self,naam):
        self.naam = naam

    def __repr__(self):
        return f"Naam van User: {self.naam}"

db.create_all()
