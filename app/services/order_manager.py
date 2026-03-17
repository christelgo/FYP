import uuid
from flask import session
from datetime import datetime
from app.services.delivery_service import get_lalamove_price

TEMP_ORDERS= {}

def create_draft_order(cart, customer_name, customer_phone,order_type, postal_code,zone,address, outlet_id, outlet_name):
    order_id = str(uuid.uuid4())
    subtotal = calculate_total(cart)
    order = {
        "id" : order_id,
        "items": cart,
        "status":"DRAFT",
        "subtotal":subtotal,
        "created_at": datetime.utcnow(),
        "customer_name": customer_name,
        "customer_phone": customer_phone,
        "order_type": order_type,
        "postal_code":postal_code,
        "zone": zone,
        "address":address,
        "outlet_id" : outlet_id,
        "outlet_name": outlet_name,   
        "delivery_fee": 0,
        "final_total": 0,

    }

    TEMP_ORDERS[order_id] = order
    return order

def get_order(order_id):

    return TEMP_ORDERS.get(order_id)

def calculate_total(cart):
    total = 0.0
    for item in cart :
        base_price = float(item.get("base_price",0))
        add_on_price = float(item.get("add_on_price",0))
        quantity = int(item.get("quantity", 1))
        total += (base_price + add_on_price)* quantity
    return round(total, 2)