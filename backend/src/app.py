from flask import Flask
from flask_cors import CORS
import logging
from api.models import db
# from api.routes import routes

from config import APP_CONFIG


# def register_blueprints(app):
    # app.register_blueprint(routes)


# def init_extensions(app):
#     logging.basicConfig(level=logging.DEBUG)
#     db.init_app(app)
#     CORS(
#         app,
#         supports_credentials=True,
#         resources=r"/*",
#     )
#     with app.app_context():
#         db.create_all()


app = Flask(__name__)
app.config.from_object(APP_CONFIG)
print(app.config)
# register_blueprints(app)
# init_extensions(app)

# command to run application: FLASK_ENV=development python -m flask run
if __name__ == '__main__':
    app.run(debug=True)