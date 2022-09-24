
from flask_login import UserMixin

from . import db


# class Payment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     credits = db.Column(db.Float,default=0, nullable=False)
#     validation = db.Column(db.Boolean,default=False)



class Users(db.Model,UserMixin):
    #  __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    registration = db.Column(db.String(100), unique=True, nullable=False)
    credits = db.Column(db.Float,default=0, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    # def __init__(self,name,registration,credits,password):
    #     self.name = name
    #     self.registration = registration
    #     self.credits = credits
    #     self.password = password




