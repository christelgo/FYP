from flask import request
from  app.models import Order, Customization, OrderItem
from app import db

def create_order_from_data(data):

    new_order = Order(
            order_type = data['Order_Type'],
            customer_name = data['customer_name'],
            customer_phone = data['customer_phone'],
            postal_code=data['postal_code'],
            zone = data['zone'],
            delivery_address= data['delivery_address'],
            total_amount = data[ 'total_amount'],
            created_at = data['created_at'],
            status = data['status']
        )
    db.session.add(new_order)
    db.session.flush()

    for item in data['items']:
        order_item = OrderItem(
        order_id=new_order.id,
        item_name = item['item_name'], 
        quantity = item['quantity']
        )
        db.session(order_item)
        db.session.flush()
        
        for custom in item['customizations']:
            customization = Customization(
                order_item_id=order_item.id,
                option_name = custom['option_item'],
                option_value = custom['option_value'],
                option_price = custom['option_price']
                )
            db.session.add(customization)

        db.session.commit()

        return new_order