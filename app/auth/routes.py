from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.auth.authform import RegistrationForm, LoginForm
from app.auth import bp
from app.models.user import Users
from app.extensions import db
from datetime import datetime



def time12hour(time):
    # convert time to date time object
    time_object = datetime.strptime(str(time), "%H:%M:%S")
    # Format it to 12 hour tie with AM/PM
    return time_object.strftime("%I:%M:%S %p")



@bp.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        # print(form.date_time.data)
        # print(form.date_field.data)
        # print(form.time_field.data)
        
        # print(time12hour(form.time_field.data))
       
        new_user = Users(f_name=form.f_name.data,l_name=form.l_name.data, phone=form.phone.data, password=generate_password_hash(form.password.data))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/registration.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
       
        user = Users.query.filter_by(phone=form.phone.data).first()
        
        if user:
           
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                # return redirect(url_for('main.index'))
                if user.role=='admin':
                    return redirect(url_for('admin.index'))
                else:
                    return redirect(url_for('main.index'))
            else:
                flash('Please check your login credential and try again')
                return redirect(url_for('auth.login'))
           
    return render_template('auth/login.html', form=form)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))