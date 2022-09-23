from flask import Flask
from flask_marshmallow import Marshmallow
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine





from app.view import views
from app.auth import auth


def create_app():
    app = Flask(__name__,static_folder = "./static",template_folder = "./templates")
    app.secret_key = 'super secret key'

    ma = Marshmallow(app)



    #Configurate
    engine = create_engine('mysql+pymysql://root:root@localhost:3306/recharge')
    Base = declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()


    #Routes pages
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
