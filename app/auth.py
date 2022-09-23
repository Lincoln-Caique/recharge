from crypt import methods
from unicodedata import category
from xmlrpc.client import boolean
from flask import Blueprint, render_template, request,flash, url_for,redirect

from  werkzeug.security import generate_password_hash, check_password_hash
from .models import Users
from . import session



auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template("login.html", boolean=True)


@auth.route('/sign_up',methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        registration = request.form.get('registration')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(registration) < 11:
            flash('Identificação única incorreta.', category='error')
        elif len(name) == 0:
            flash('Nome válido deve ter mais caracteres.', category='error')
        elif password1 != password2:
            flash('Senhas utilizadas nao são iguais.', category='error')
        else:
            new_user = Users(name=name,registration=registration,password=generate_password_hash(password1, method='sha256'),credits=0)
            session.add(new_user)
            session.commit()
            session.close()
            flash('Conta criada!', category='success')
            return redirect(url_for('views.home'))
          


    return render_template("sign_up.html")
