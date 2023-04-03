from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, static_folder='../static', url_prefix='/users')

USERS = {
    1: 'Alice',
    2: 'John',
    3: 'Mike'
}


@user.route('/')
def user_list():
    return render_template(
        'users/list.html',
        users=USERS
    )


@user.route('/<pk>')
def get_user(pk: int):
    pk = int(pk)
    try:
        user_name = USERS[pk]
    except KeyError:
        # raise NotFound(f'User id {pk} not found')
        return redirect('https://www.yandex.ru/')  # redirected to another urls
    return render_template(
        'users/detail.html',
        user_name=user_name
    )
