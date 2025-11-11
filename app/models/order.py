from app import db
from datetime import datetime

class Order(db.Model):
    __tablename__='orders'

    id= db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable = False)
    cutsomer_phone = db.Column(db.String(20))