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
    delivery_address = db.Column(db.String())
    total_amount = db.Column(db.Float)
    created_at = db.Column(db.DateTime , default=datetime.utcnow)
    status =db.Column(db.String(20), default='DRAFT')

    items = db.relationship(
        "OrderItem",
        back_populates = "order",
        cascade = "all, delete-orphan"
    )
    
class OrderItem(db.Model):
    __tablename__="order_items"

    id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))

    menu_item_id = db.Column(db.Integer, db.ForeignKey("menu_items.id"))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)

    order = db.relationship("Order", back_populates="items")
    customisations = db.relationship(
        "Customization",
        back_populates = "order_item",
        cascade="all, delete-orphan"
    )

class Customization(db.Model):
    __tablename__ = "customizations"

    id = db.Column(db.Integer, primary_key=True)

    order_item_id = db.Column(
        db.Integer,
        db.ForeignKey("order_items.id"),
        nullable = False
    )

    name = db.Column(db.String(50), nullable= False)
    value = db.Column(db.String(50), nullable = False)

    order_item = db.relationship(
        "OrderItem",
        back_populates = "customisations", 
    )


    

