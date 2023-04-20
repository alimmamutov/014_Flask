from flask import Blueprint, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, static_folder='../static', url_prefix='/users')

USERS = {
    1: 'Alice',
    2: 'John',
    3: 'Mike'
}


@user.route('/')
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users
    )


@user.route('/<int:pk>')
@login_required
def profile(pk: int):

    # try:
    # user_name = USERS[pk]
    from blog.models import User
    _user = User.query.filter_by(id=pk).one_or_none()
    # raise NotFound(f'User id {pk} not found')
    if not _user:
        raise NotFound(f'User id {pk} not found')
        # return redirect('https://www.yandex.ru/')  # redirected to another urls
    return render_template(
        'users/detail.html',
        user=_user
    )
