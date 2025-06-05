from flask import Flask
from extensions import db, migrate, cors
from routes.authentication import authentication_bp
from routes.users import users_bp
from routes.group import groups_bp
from routes.groupmembers import groupmembers_bp

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
#app configuration    
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db.init_app(app)
migrate.init_app(app, db)
cors.init_app(app)

app.register_blueprint(authentication_bp)
app.register_blueprint(users_bp)
app.register_blueprint(groups_bp)
app.register_blueprint(groupmembers_bp)

@app.route('/')
def hello():
    return "Hello, Proxima Centauri!"

if __name__ == '__main__':
    app.run(debug=True)