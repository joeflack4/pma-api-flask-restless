import os

# From Boilerplate
DEBUG = True
SECRET_KEY = 'my precious'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
HOST = 'localhost'
PORT = int(os.environ.get('PORT', 5000))

# From my app.
DEVELOPMENT = True
TESTING = False
CSRF_ENABLED = True
WTF_CSRF_ENABLED = True
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = True
