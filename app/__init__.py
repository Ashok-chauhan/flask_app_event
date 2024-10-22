from flask import Flask

from config import Config
from app.extensions import db
from flask_login import LoginManager
from app.models.user import Users
import os


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    app.config['UPLOAD_DIRECTORY'] = 'uploads/'  #'./app/static/images/'
    # app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024 #16 MB
    app.config['ALLOWED_EXTENTIONS'] = ['.jpg', 'jpeg', '.png', '.gif', '.pdf']
   
    # Initialize Flask extensions here
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.posts import bp as post_bp
    app.register_blueprint(post_bp, url_prefix='/posts')

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')


    @app.route('/test/')
    def test_page():
        return '<h1> Testing the Flask Application Factory Pattern</h1>'
    
    return app
