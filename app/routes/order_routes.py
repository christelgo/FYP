from flask import Blueprint, request, jsonify
from app.models import Order, Customization
from app import db

order_bp = Blueprint('order_bp', __name__, url_prefix = '/api/orders')

@order_bp.route('/', methods=['POST'])
def create_order():
    data = request.get_json()

    new_order = Order(
        id = db.Column(),
        order_type = data['Order_Type'],
        customer_name = data['Customer_name'],
        customer_phone = data['Customer_phone'],
        postal_code=['Postal_code'],
        zone = data['Zone'],
        delivery_address= data['delivery_address'],
        total_amount = data[ 'Total_amount']
    )
    db.session.add(new_order)
    db.session.commit()

    for item in data['items']:
        order_item = Order(
            order_id=new_order.id,
            item_name = item['item_name'], 
            quantity = item['quantity']
        )
        db.session(order_item)
        db.session.commit()

        for custom in item['customizations']:
            customization = Customization(
                order_item_id=order_item.id,
                name=custom
            )
            db.session.add(customization)

    db.session.commit()
    return jsonify ({"message": "Order Created", "order_id":new_order.id}), 201