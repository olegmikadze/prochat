from flask import Flask
from flask_cors import CORS
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text
from api.models import db, User
# from api.routes import routes

from config import APP_CONFIG


# def register_blueprints(app):
    # app.register_blueprint(routes)


# def init_extensions(app):
    # logging.basicConfig(level=logging.DEBUG)
    # db.init_app(app)
    # CORS(
    #     app,
    #     supports_credentials=True,
    #     resources=r"/*",
    # )
    # with app.app_context():
    #     db.create_all()


app = Flask(__name__)
app.config.from_object(APP_CONFIG)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1@localhost:5432/prochat'

db = SQLAlchemy(app)

print(db)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    nickname = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    phone = db.Column(db.Text, nullable=False, unique=True)

# register_blueprints(app)
# init_extensions(app)

# command to run application: FLASK_ENV=development python -m flask run
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
