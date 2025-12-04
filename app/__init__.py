from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app= Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from app.routes.chatbot_routes import chatbot_bp
    from app.routes.menu_routes import menu_bp
    from app.routes.order_routes import order_bp

    app.register_blueprint(chatbot_bp, url_prefix='/api/chat')
    app.register_blueprint(menu_bp, url_prefix='/api/menu')
    app.register_blueprint(order_bp,url_prefix='/api/orders' )
    
# Note for later: I wanna get rid of the /api as I feel like it is redundant
    return app