class Config:
    DEBUG = False


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    TESTING = True
    SECRET_KEY = 'x!8lcxs34a%!x-h!cxc2xajsc2+y*70-&%dq@5@_4pw%j9a5o*'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
