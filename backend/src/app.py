from flask import Flask
from flask_cors import CORS
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from api.routes import routes

from config import APP_CONFIG


def register_blueprints(app):
    app.register_blueprint(routes)

app = Flask(__name__)
app.config.from_object(APP_CONFIG)
db = SQLAlchemy()
migrate = Migrate()

db.init_app(app)

migrate.init_app(app, db)

from api.models import User

register_blueprints(app)



# flask db init (once) by creating
# creating table in DB
# flask db migrate -m "{name}" 
# flask upgrade

