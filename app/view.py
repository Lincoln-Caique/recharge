from crypt import methods
from flask import Blueprint, render_template, flash, request
from flask_login import login_required, current_user

from . import db

views = Blueprint('views', __name__)


@views.route('/')
# def index():
#     return render_template("index.html")

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        pass
    
    return render_template("home.html", user=current_user)

@views.route('/about')
def about():
    return render_template("about.html")
