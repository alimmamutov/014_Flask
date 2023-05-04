from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash

from blog.app import login_manager

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=('GET',))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    return render_template(
        'auth/login.html',
    )


@auth.route('/login', methods=['POST',])
def login_post():
    from blog.models import User

    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('Check your login details')
        return redirect(url_for('.login'))
        # return f'{email} {password}'
    else:
        login_user(user)
        return redirect(request.form.get("submit_button") or url_for('user.profile', pk=user.id))
        # return redirect(request.referrer)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
