from flask import Blueprint, render_template

report = Blueprint('report', __name__, static_folder='../static', url_prefix='/reports')


@report.route('/')
def report_list():
    return render_template('reports/list.html', reports=['report1', 'report2', 'report3', 'report4'])
