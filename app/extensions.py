from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

env = load_dotenv()
db = SQLAlchemy()