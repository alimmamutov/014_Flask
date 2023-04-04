from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

from blog.user.views import USERS

article = Blueprint('article', __name__, static_folder='../static', url_prefix='/articles')

ARTICLES = {
    1: {
        'title': 'Python for juniors',
        'text': 'Donald Trump personally pleaded not guilty in a Manhattan court to 34 felony counts of falsifying'
                'business records in the first degree after hearing charges against him stemming from a hush money '
                'payment to an adult film actress in 2016.',
        'user_id': 1
    },
    2: {
        'title': 'Charging documents',
        'text': 'The grand jury indictment has been unsealed and CNN is going through it now. You can read the full '
                'document',
        'user_id': 1
    },
    3: {
        'title': 'The statement of facts',
        'text': 'Prosecutors allege Trump was a part of an "illegal conspiracy" to undermine the integrity of the 2016'
                'election and was part of an unlawful plan to suppress negative information.',
        'user_id': 2
    },
    4: {
        'title': 'Charging documents put Trump',
        'text': 'Manhattan prosecutors have placed Donald Trump at the center of an alleged "catch and kill" scheme to'
                'suppress negative stories',
        'user_id': 2
    },
    5: {
        'title': 'AMI did not vet the story before purchasing',
        'text': 'When they concluded the story was not true, AMI wanted to release the doorman',
        'user_id': 3
    },
    6: {
        'title': 'Biden’s claim that ‘you’re not allowed’',
        'text': 'Biden made the claim while delivering a plea for a renewed ban',
        'user_id': 2
    },
}


@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES, users=USERS
    )


@article.route('/<int:pk>')
def get_article(pk: int):
    data = ARTICLES[pk]
    data['username'] = USERS[data['user_id']]
    # try:
    #     user_name = USERS[pk]
    # except KeyError:
    #     # raise NotFound(f'User id {pk} not found')
    #     return redirect('https://www.yandex.ru/')  # redirected to another urls
    return render_template(
        'articles/detail.html',
        data=data
    )
