import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-2.5-flash")

BOT_SESSIONS = {}

# =====================
# MAIN BOT ENGINE
# =====================
def generate_bot_reply(session_id, message, customer_phone=None):
    message = message.strip()
    msg_lower = message.lower()
    words = msg_lower.split()

    # ------------------------------------
    # Init session
    # ------------------------------------
    if session_id not in BOT_SESSIONS:
        BOT_SESSIONS[session_id] = {
            "customer_phone": None,
            "reservation": {
                "outlet": None,
                "date": None,
                "time": None,
                "pax": None,
                "special_requests": None,
                "confirmed": False
            }
        }

    session_data = BOT_SESSIONS[session_id]

    # Upgrade phone when it becomes available
    if customer_phone:
        session_data["customer_phone"] = customer_phone

    res = session_data["reservation"]

    # =====================
    # QUICK INTENTS
    # =====================
    if any(w in words for w in ["hi", "hello", "hey"]):
        return "Hello! 😊 How may I help you today?"

    if "menu" in words:
        return "Here is our menu: http://127.0.0.1:5000/menu"

    if any(w in words for w in ["order", "buy", "makan", "purchase"]):
        return (
            "Certainly! 🍗\n"
            "Here is the order form:\n"
            "http://127.0.0.1:5000\n\n"
            "You can submit your PayNow screenshot after ordering."
        )

    # =====================
    # RESERVATION FLOW
    # =====================
    if any(w in words for w in ["reserve", "reservation", "book", "booking", "table", "dine"]):
        reset_reservation(res)
        return "Sure 😊 Which outlet would you like to reserve at?"

    if res["outlet"] is None:
        res["outlet"] = message.title()
        return "Got it 👍 What date would you like to come? (e.g. 12 Feb)"

    if res["date"] is None:
        res["date"] = message
        return "Nice! What time should I reserve for you? (e.g. 7:30 PM)"

    if res["time"] is None:
        res["time"] = message
        return "How many pax will be dining?"

    if res["pax"] is None:
        res["pax"] = message
        return (
            "Any special requirements?\n"
            "Examples: baby chair, indoor/outdoor seating.\n"
            "Reply *none* if not applicable."
        )

    if res["special_requests"] is None:
        res["special_requests"] = message
        return generate_reservation_summary(res)

    if "confirm" in words:
        res["confirmed"] = True
        route_reservation(res)
        return "✅ Your reservation is confirmed! We’ve informed the outlet."

    # =====================
    # FALLBACK
    # =====================
    return "I’m sorry 😅 could you rephrase that?"

# =====================
# HELPERS
# =====================
def reset_reservation(res):
    res.update({
        "outlet": None,
        "date": None,
        "time": None,
        "pax": None,
        "special_requests": None,
        "confirmed": False
    })

def generate_reservation_summary(res):
    return (
        "📋 *Reservation Summary*\n"
        f"Outlet: {res['outlet']}\n"
        f"Date: {res['date']}\n"
        f"Time: {res['time']}\n"
        f"Pax: {res['pax']}\n"
        f"Special requests: {res['special_requests']}\n\n"
        "Reply *CONFIRM* to finalize your reservation."
    )

def route_reservation(res):
    print("📢 NEW RESERVATION")
    print(res)

# =====================
# MESSAGE SENDER
# =====================
def send_bot_message(to, message):
    print(f"[BOT → {to}] {message}")