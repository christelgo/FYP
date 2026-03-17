from flask import Blueprint, request, jsonify, session
import uuid

from app.services.bot_engine import generate_bot_reply, send_bot_message

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}

    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400


    if "chat_session_id" not in session:
        session["chat_session_id"] = str(uuid.uuid4())

    session_id = session["chat_session_id"]


    customer_phone = session.get("customer_phone")  # None is OK


    reply = generate_bot_reply(
        session_id=session_id,
        message=user_message,
        customer_phone=customer_phone
    )

    # ------------------------------------
    # 4️⃣ Send message (console for now)
    # ------------------------------------
    send_bot_message(
        to=customer_phone or session_id,
        message=reply
    )

    return jsonify({"reply": reply})
