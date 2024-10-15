import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABSE_URI')\
    or 'mysql+pymysql://flask:FlaskApp@9@127.0.0.1/events'
    #or 'mysql+pymysql://root:@localhost/events'
    #or 'sqlite:///'+ os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # UPLOAD_DIRECTORY = 'uploads/'
    # MAX_CONTENT_LENGTH = 16*1024*1024 #16 MB
    # ALLOWED_EXTENTIONS = ['.jpg', 'jpeg', '.png', '.gif', '.pdf']
