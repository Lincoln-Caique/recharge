
from sqlalchemy import Column, String, Integer,Float
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base


from . import create_app

app = create_app()



class Users(app.Base,UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    registration = Column(String(100), unique=True, nullable=False)
    credits = Column(Float,default=0, nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self,name,registration,credits,password):
        self.name = name
        self.registration = registration
        self.credits = credits
        self.password = password



class UserSchema(app.ma.Schema):
    class Meta:
        fields = ("id", "name", "registration","credits","password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)


