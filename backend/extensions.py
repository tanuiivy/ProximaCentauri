# This file contains the Flask extensions used in the app.
#separated them since i was getting circular import errors
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
