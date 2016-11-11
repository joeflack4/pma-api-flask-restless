import os
import logging
from flask import Flask, request as req
from app.controllers import pages
# flask.ext is deprecated.
# from flask.ext.restless import APIManager
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from .config import Config
from .api import ApiAuth


app = Flask(__name__)

app.register_blueprint(pages.blueprint)
app.logger.setLevel(logging.NOTSET)
# For some reason, config is not pulling properly.
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Need to remove this in production. For testing only.
# print(str(app.config))

db = SQLAlchemy(app)
from .models import AppConfig

# try:
#     app.config.from_object(os.environ['APP_SETTINGS'])
# except KeyError:
#     # If environment variable 'APP_SETTINGS' isn't defined by administrator, exception defaults to development settings.
#     app.config.from_object(config.DevelopmentConfig)
# except:
#     # Backup exception.
#     app.config.from_object(config.DevelopmentConfig)



######################
###      API       ###
######################
api_manager = APIManager(app, flask_sqlalchemy_db=db)

# - API's accessible to all.
# Blank

# - API's requiring super admin status.
app_config_api_blueprint = api_manager.create_api(AppConfig, collection_name='app-config', methods=['GET', 'POST',
                                                                                                    'DELETE', 'PUT'],
                                                  preprocessors=dict(GET_SINGLE=[ApiAuth.super_admin],
                                                                     GET_MANY=[ApiAuth.super_admin]))


def create_app(config_filename):
    app.config.from_object(config_filename)


    ######################
    ###     Routes     ###
    ######################
    @app.after_request
    def log_response(resp):
        app.logger.info("{} {} {}\n{}".format(
            req.method, req.url, req.data, resp)
        )
        return resp

    return app
