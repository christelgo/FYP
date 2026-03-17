import pytesseract
from PIL import Image, ImageOps, ImageEnhance
import re

def load_image(image_path):

    img = Image.open(image_path)
    img = ImageOps.exif_transpose(img)
    return img

def image_preprocessing(img):
    img = img.convert("L")
    img = ImageEnhance.Contrast(img).enhance(2.0)
    return img

def extract_text_from_image(image_path):
    img = load_image(image_path)
    img = image_preprocessing(img)

    text = pytesseract.image_to_string(img)
    return text.lower()

def normalize_amount(amount):
    amt = float(amount)
    return [
        f"{amt:.2f}",
        f"{amt:.1f}",
        f"{amt:.2f}".replace(".",","),
    ]

# def validate_paynow_image(image_path, order):
#     text = extract_text_from_image(image_path)

#     expected_recipient = ""  
#     if isinstance(order, dict):
#         final_amount = order["final_amount"]

#     expected_amount = normalize_amount(order["final_amount"])

#     if expected_recipient not in text:
#         return {
#             "valid":False,
#             "reason": "Wrong recipient"
#         }
#     amount_found = any ( amt in text for amt in expected_amount)
#     if not amount_found:
#         return{
#             "valid": False,
#             "reason": "Incorrect payment amount"
#         } 
#     return {
#         "valid":True,
#         "extracted text": "Payment verified thank you for your order "
#     }