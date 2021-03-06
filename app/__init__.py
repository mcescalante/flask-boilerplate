import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_script import Manager
from flask_wtf.csrf import CSRFProtect
from .config import _basedir

# App
app = Flask(__name__)
config = app.config.from_object('app.config')

# Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

# Login & Forms
lm = LoginManager()
lm.init_app(app)
CSRFProtect(app)

# Mail
if app.config['USE_MAIL'] is True:
  from sparkpost import SparkPost
  sp = SparkPost()
else:
  pass

# Blueprints
from app.account.views import accounts as accounts
app.register_blueprint(accounts)

from app import models, views