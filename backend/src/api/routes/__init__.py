from flask import Blueprint

routes = Blueprint('routes', __name__)

# add a file you want to write code in, for instance zaebis.py
# ADD IT HERE
# then add here:
# from .zaebis import zaebis1, zaebis2 ...
from .signup import signup
from .signin import signin
from .facebook import signin_fb
from .google import signin_google
from .setting import settings
from .notification import notification
from .profile import profile
