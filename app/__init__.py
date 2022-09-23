from flask import Flask
from flask_marshmallow import Marshmallow
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,Column, String, Integer,Float
from flask_login import UserMixin





def create_app():
    from app.view import views
    from app.auth import auth

    app = Flask(__name__,static_folder = "./static",template_folder = "./templates")
    app.secret_key = 'super secret key'

    # ma = Marshmallow(app)


    #Routes pages
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app





Base = declarative_base()

#Configurate
engine = create_engine('mysql+pymysql://root:root@localhost:3306/recharge')
# Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()





# class Users(Base,UserMixin):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(80), nullable=False)
#     registration = Column(String(100), unique=True, nullable=False)
#     credits = Column(Float,default=0, nullable=False)
#     password = Column(String(100), nullable=False)

#     def __init__(self,name,registration,credits,password):
#         self.name = name
#         self.registration = registration
#         self.credits = credits
#         self.password = password



# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ("id", "name", "registration","credits","password")

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)


