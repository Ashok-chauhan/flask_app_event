import sys
from dotenv import load_dotenv


sys.path.insert(0, '/var/www/flask_app_event')
sys.path.insert(0, '/var/www/flask_app_event/myenv/lib/python3.10/site-packages')
load_dotenv()
from app import create_app
application = create_app()


