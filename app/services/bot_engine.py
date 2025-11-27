import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-2.5-flash")

def generate_bot_reply(message):
    message = message.lower().strip()
    words = message.split()


    if "order" in words:
        return (
            "Certainly! Here is the order form: (link appears here).\n"
            "Please submit your PayNow payment screenshot."
        )

    if "menu" in words:
        return "Here is the menu."

    if "hi" in words or "hello" in words:
        return "Hello! How may I help you?"

    if "submitted" in words:
        return "Thank you! We have received your order."


    prompt = f"""
    You are an F&B restaurant chatbot. Your job is to correctly understand the customer's intent,
    even if they use slang, wrong spelling, different tenses, or indirect language.

    Customer message: "{message}"

    Determine the correct INTENT:
    1. ORDERING — user wants to place an order, buy food, makan, purchase something
    2. MENU — user wants to see the menu
    3. GREETING — user is greeting
    4. CONFIRMATION — user says they submitted payment or confirmed something
    5. UNKNOWN — unclear intent

    Reply ONLY with:
    - If ORDERING → "Certainly! Here is the order form: (link). Please submit your payment screenshot."
    - If MENU → "Here is the menu."
    - If GREETING → "Hello! How may I help you?"
    - If CONFIRMATION → "Thank you! We have received your order."
    - If UNKNOWN → "I'm sorry, could you clarify what you mean?"

    Respond ONLY with the final answer. No explanations.
    """

    try:
        response = model.generate_content(prompt)
        return response.text   

    except Exception as e:
        print("LLM Error:", e)

    
    
    return "I'm sorry, I didn't quite catch that. Can you repeat?"
