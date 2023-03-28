from flask import Blueprint

report = Blueprint('report', __name__, static_folder='../static', url_prefix='/reports')


@report.route('/')
def user_list():
    return 'hello rep'
