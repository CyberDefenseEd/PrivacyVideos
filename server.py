from quart import Quart
from apscheduler.schedulers.background import BackgroundScheduler
from routes import home_bp, video_bp
from util import fetch_homepage
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

app = Quart(__name__, static_folder='/assets/static')

app.register_blueprint(home_bp)
app.register_blueprint(video_bp)

# Set up scheduler for fetching featured every 5min 
scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_homepage, trigger='interval', minutes=5)
scheduler.start()

fetch_homepage()

if __name__ == '__main__':
    app.run(debug=False)
