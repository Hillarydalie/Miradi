from flask import Flask
from config import configurations
from flask_login import login_manager,LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES

app =  Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"
photos = UploadSet('photos', IMAGES)

def create_app(config_name):
    app.config.from_object(configurations[config_name])
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    db.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app,photos)
    return app
