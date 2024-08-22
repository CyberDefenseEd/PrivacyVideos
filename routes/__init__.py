from quart import Blueprint

home_bp = Blueprint('home', __name__)
video_bp = Blueprint('video', __name__)

from . import home, video
