from app import db

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50))
    #zone_id = db.Column(db.Integer,db.ForeignKey('outlet_zones.id'))

    #def __repr__(self):
        #return f"<MenuItem {self.name}>"