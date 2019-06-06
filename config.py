import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Get database URL from the DATABASE_URL environment variable
    # if DATABASE_URL is not defined
    # Configure a database named app.db located in the main directory of the application, which is stored in the basedir variable.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
