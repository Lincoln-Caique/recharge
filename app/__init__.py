from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager



db = SQLAlchemy()
DB_Name = "recharge"


def create_app():
    app = Flask(__name__,static_folder = "./static",template_folder = "./templates")
    app.config['SECRET_KEY'] = 'lincoln'
    app.config['SQLALCHEMY_DATABASE_URI'] =  f'mysql+pymysql://root:root@localhost:3306/{DB_Name}'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']   = False
    db.init_app(app)
    
    from app.view import views
    from app.auth import auth

    #Routes pages
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Users



    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app







