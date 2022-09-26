from crypt import methods
from curses.ascii import isdigit
from flask import Blueprint, render_template, flash, request
from flask_login import login_required, current_user

from . import db
from .models import Users

views = Blueprint('views', __name__)




@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        credits = request.form.get('credits')
        current_user.credits = current_user.credits + float(credits)
        db.session.commit()
        flash(f'Recarga em análise!', category="success")
        # if type(credits) == int:
        #     print(f'SOU NÚMERO PORRA {credits}')
        #     flash('Recarga em análise!', category="success")
        # else:
        #     flash('Digite um valor válido!', category="error")
    
    return render_template("home.html", user=current_user)

@views.route('/about')
def about():
    return render_template("about.html")
