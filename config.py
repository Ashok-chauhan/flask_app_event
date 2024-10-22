import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ashok975'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABSE_URI')\
    or 'mysql+pymysql://flask:FlaskApp_9@localhost/events'
    # or 'mysql+pymysql://root:@localhost/eventsx'
    #or 'sqlite:///'+ os.path.join(basedir, 'app.db')
    # UPLOAD_DIRECTORY = 'uploads/'
    # MAX_CONTENT_LENGTH = 16*1024*1024 #16 MB
    # ALLOWED_EXTENTIONS = ['.jpg', 'jpeg', '.png', '.gif', '.pdf']
