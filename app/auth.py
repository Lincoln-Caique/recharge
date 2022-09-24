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
    if request.method == 'POST':
        registration = request.form.get('registration')
        password = request.form.get('password')

        user = session.query(Users).filter_by(registration=registration).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Login realizado com sucesso', category='sucess')
            else:
                flash('Senha incorreta, tente novamente', category='error')

        else:
            flash('Identificação única não existe.', category='error')

    return render_template("login.html", boolean=True)


@auth.route('/sign_up',methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        registration = request.form.get('registration')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = session.query(Users).filter_by(registration=registration).first()

        if user:
            flash('Identificaão única existente', category='error')
        elif len(registration) < 11:
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
