from flask import Blueprint, request, jsonify
from app.services.bot_engine import generate_bot_reply

chatbot_bp = Blueprint('chatbot_bp', __name__)

@chatbot_bp.route("/", methods = ["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message","")
    reply = generate_bot_reply(user_message)
    
    return jsonify({"reply":reply})