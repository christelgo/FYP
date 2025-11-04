from app import db

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)
    category = db.Column(db.String(50), default="Ala Carte")

    def __repr__(self):
        return f"<MenuItem {self.name}>"