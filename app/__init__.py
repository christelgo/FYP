from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from .config import Config
#from app.routes.chatbot_routes import chatbot_bp
#from app.routes.menu_routes import menu_bp

db = SQLAlchemy()

def create_app():
    app= Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)

    from app.routes.chatbot_routes import chatbot_bp
    from app.routes.menu_routes import menu_bp

    app.register_blueprint(chatbot_bp, url_prefix='/api')
    app.register_blueprint(menu_bp, url_prefix='/api')
# Note for later: I wanna get rid of the /api as I feel like it is redundant
    return app