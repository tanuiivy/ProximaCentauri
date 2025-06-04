from flask import Flask
from extensions import db, migrate, cors
from routes.authentication import authentication_bp

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
cors.init_app(app)

app.register_blueprint(authentication_bp, url_prefix='/auth')

@app.route('/')
def hello():
    return "Hello, Proxima Centauri!"

if __name__ == '__main__':
    app.run(debug=True)