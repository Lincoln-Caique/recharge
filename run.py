from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, String, Integer,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_marshmallow import Marshmallow





app = Flask(__name__,static_folder = "./app/static",template_folder = "./app/templates")

ma = Marshmallow(app)



#Configurate
engine = create_engine('mysql+pymysql://root:root@localhost:3306/recharge')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#Entities
class Users(Base):
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



class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "registration","credits","password")

user_schema = UserSchema()
users_schema = UserSchema(many=True)




@app.route('/')
def index():
    return render_template("index.html")



#Create
@app.route('/users', methods=['POST'])
def create_user():
  body = request.get_json()
  session.add(Users(body['name'], body['registration'], body['credits'], body['password']))
  session.commit()
  return "User created"

#Read user
@app.route('/users/<registration>', methods=['GET'])
def read_user(registration):
    user =  session.query(Users).filter(Users.registration == registration)
    return users_schema.jsonify(user)

#Read many users
@app.route('/users', methods=['GET'])
def read_users():
    users =  session.query(Users).all()
    return users_schema.jsonify(users)


#Update informations
@app.route("/users/<registration>",methods=["PUT"])
def update_password(registration):
    body = request.get_json()
    session.query(Users).filter(Users.registration==registration).update(dict(password=body['password']))
    session.commit()
    session.close()
    return "Update password"    

#Update credits
@app.route("/users/credits/<registration>",methods=["PUT"])
def update_credits(registration):
    body = request.get_json()
    session.query(Users).filter(Users.registration==registration).update(dict(credits=body['credits']))
    session.commit()
    session.close()
    return "Update credits"


#Delete
@app.route("/delete/<registration>",methods=["DELETE"])
def delete_user(registration):
    user = session.query(Users).filter(Users.registration==registration).delete()
    session.commit()
    session.close()
    return user_schema.jsonify(user)





if __name__ == '__main__':
    app.run(debug=True)
