from app import db
from datetime import datetime

class Order(db.Model):
    __tablename__ ='orders'

    id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.String(), nullable=False)
    customer_phone= db.Column(db.String())
    order_type = db.Column(db.String())

    items = db.relationship('OrderItem', backref='order', lazy=True)
    customizations = db.relationship(
        'Customization', backref='order_item', cascade="all, delete"
    )
    def to_dict(self):
        return{
            "id": self.id,
            "customer_name": self.customer_name,
            "customer_phone": self.customer_phone,
            "created_at": self.created_at.isoformat()
        }
    def __repr__(self):
        return f"<Order {self.id} - {self.customer_name}>"