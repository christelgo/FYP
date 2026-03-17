from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app= Flask(__name__)
    app.config.from_object("app.config.Config")
    db.init_app(app)

    from app.routes.chatbot_routes import chatbot_bp
    from app.routes.menu_routes import menu_bp
    from app.routes.order_routes import order_bp
    from app.routes.postal_routes import postal_bp
    from app.routes.main_routes import main_bp
    from app.routes.payment_route import payment_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(chatbot_bp, url_prefix='/api/chat')
    app.register_blueprint(menu_bp, url_prefix='/api/menu')
    app.register_blueprint(order_bp,url_prefix='/api/orders' )
    app.register_blueprint(postal_bp,url_prefix ="/api/postal")
    app.register_blueprint(payment_bp, url_prefix="/api/payment")
    
# Note for later: I wanna get rid of the /api as I feel like it is redundant
    return app