from flask import Flask
from app.config.db import db

def create_app(config):
    app = Flask(__name__ , template_folder="views")    
    app.config.from_object(config)
    
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app