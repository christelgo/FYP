from flask import Blueprint, jsonify

menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/menu", methods=["GET"])
def get_menu():
    temp_menu =[
        {"id":1, "name": "Burger", "price": 5.99},
        {"id":2, "name": "Fries", "price":2.99},
        {"id":3, "name": "Sprite", "price":1.99}
    ]
    return jsonify({"menu":temp_menu}),200