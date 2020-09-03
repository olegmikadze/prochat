from flask import Blueprint
from flask_socketio import SocketIO

routes = Blueprint('routes', __name__)

# Initialize sockets here to have an access to them
# from an endpoints (configured with app in app.py)
socketio = SocketIO()

# add a file you want to write code in, for instance zaebis.py
# ADD IT HERE
# then add here:
# from .zaebis import zaebis1, zaebis2 ...

from .signup import signup
from .signin import signin
from .facebook import signin_fb
from .google import signin_google
from .main_page import get_events, get_filters
from .setting import settings
from .notification import notification
from .profile import profile
