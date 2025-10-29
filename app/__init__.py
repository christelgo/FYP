from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from app.routes.chatbot_routes import chatbot_bp

db = SQLAlchemy()

def create_app():
    app= Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(chatbot_bp, url_prefix='/api')

    return app