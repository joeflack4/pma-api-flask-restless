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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)
from .models import AppConfig

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


def create_app(config_filename, app):
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
