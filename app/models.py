from app import db
from flask_sqlalchemy import declarative_base
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
# from datetime import datetime
# - Deprecations: flask.ext has been deprecated.
# from sqlalchemy.ext.declarative import declarative_base

db.Base = declarative_base()

# - To Do: Figure out relational mapping.
# user_messages = db.Table('user_messages', db.Base.metadata,
#     db.Column('user_id', db.Integer, ForeignKey('user.id')),
#     db.Column('messages_id', db.Integer, ForeignKey('messages.id'))
# )


##############
# - Super Classes
class BaseModel(db.Model):
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now(), index=True)
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), index=True)


class BaseConfig(BaseModel):
    __abstract__ = True

    key = db.Column(db.String(100), primary_key=True, nullable=False)
    value = db.Column(db.String(200), nullable=False)
    permission_level = db.Column(db.Integer, nullable=False, index=True)
    active = db.Column(db.Boolean, nullable=False, index=True)

    def __init__(self, key, value, permission_level, active):
        self.key = key
        self.value = value
        self.permission_level = permission_level
        self.active = active

    def __repr__(self):
        return '<key name: {}>'.format(self.key)


##############
# - App Core Models
class AppConfig(BaseConfig):
    __tablename__ = 'app_config'
