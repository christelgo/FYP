from app import db
from datetime import datetime

class Order(db.Model):
    __tablename__ ='orders'

    id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.String(), nullable=False)
    customer_phone= db.Column(db.String(), nullable=False)
    order_type = db.Column(db.String())
    postal_code = db.Column(db.Integer)
    zone = db.Column(db.String())
    delivery_address = db.Column(db.String(), nullable= False)
    total_amount = db.Column(db.Float)
    created_at = db.Column(db.DateTime , default=datetime.utcnow)
    status =db.Column(db.String(20), default='Pending')

    items = db.relationship('OrderItem', backref='order', cascade="all, delete")
    
    def to_dict(self):
        return{
            "id": self.id,
            "order_type": self.order_type,
            "customer_name": self.customer_name,
            "customer_phone": self.customer_phone,
            "postal_code": self.postal_code,
            "zone" : self.zone,
            "delivery_address":self.delivery_address,
            "total_amount": self.total_amount,
            "created_at": self.created_at.isoformat(),
            "status": self.status,
            "items": [item.to_dict() for item in self.items]
        }
    def __repr__(self):
        return f"<Order {self.id} - {self.customer_name}>"
    
class OrderItem(db.Model):
    __tablename__ = 'order_items' 
    id = db.Column(db.Integer, primary_key= True)
    order_id=db.Column(db.Integer, db.ForeignKey('orders.id'))
    item_name = db.Column(db.String())
    item_price= db.Column(db.Float)
    quantity = db.Column(db.Integer)

    customizations = db.relationship('Customization', backref='order_item', cascade="all, delete")

    def to_dict(self):
        return{
            "id": self.id,
            "order_id": self.order_id,
            "item_name": self.item_name,
            "item_price": self.item_price,
            "quantity": self.quantity,
            "customization": [c.to_dict() for c in self.customizations]
        }
class Customization(db.Model):
    __tablename__='customization'

    id=db.Column(db.Integer, primary_key=True)
    order_item_id = db.Column(db.Integer, db.ForeignKey('order_items.id'))
    option_name = db.Column(db.String(100))
    option_value = db.Column(db.String(100))
    option_price = db.Column(db.Float, default=0.0)

    def to_dict(self):
        return{
            "id": self.id,
            "order_item_id": self.order_item_id,
            "option_name": self.option_name,
            "option_value": self.option_value,
            "option_price": self.option_price
        }
