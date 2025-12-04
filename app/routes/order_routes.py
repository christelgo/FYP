from flask import Blueprint, request, jsonify
from app.services import order_manager


order_bp = Blueprint('order_bp', __name__, url_prefix = '/api/orders')

@order_bp.route('/', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = order_manager.create_order(data)
    return jsonify({"message": ["Your Order has been created "] ,"order":new_order.to_dict()}),201
