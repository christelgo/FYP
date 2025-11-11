from flask import Blueprint, jsonify
from app.models.menu_items import MenuItem

menu_bp = Blueprint("menu", __name__, url_prefix="/menu")

@menu_bp.route("/menu", methods=["GET"])
def get_menu():
    items = MenuItem.query.all()
    data = [{"id":i.id, "name":i.name , "price" : i.price, "category" : i.category} for i in items]
    return jsonify(data)
#fake menu rn just so that the connections work
# will link to the menu data base