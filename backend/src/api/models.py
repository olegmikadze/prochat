from app import db

class User(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=True, unique=False)
    first_name = db.Column(db.Text, nullable=False, unique=False)
    last_name = db.Column(db.Text, nullable=False, unique=False)
    birth_date = db.Column(db.DateTime, nullable=False, unique=False)
    rating = db.Column(db.Float, nullable=True, unique=False)
    description = db.Column(db.Text, nullable=True, unique=False)
    telegram_account = db.Column(db.Text, nullable=True, unique=False)
    settings = db.Column(db.JSON, nullable=False, unique=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)