from flask import Blueprint, request, jsonify

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/chat', methods=["GET","POST"])
def chat():
    if request.method == "GET":
        return jsonify({"message": "CHATBOT API IS RUNNING"})
    
    data = request.get_json()
    user_message = data.get("message", "").lower()

    if "hello" in user_message or "hi" in user_message:
        reply = "Hello"
    else:
        reply = "Apologies could you repeat that"

    return jsonify({"reply":reply}), 200
##chatbot api runs
