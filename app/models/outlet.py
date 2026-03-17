from app import db
class Outlet(db.Model):
    __tablename__ = "outlets"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    address= db.Column(db.String(255))

    zone =db.Column(db.String(20))

    def __repr__(self):
        return f"<Outlet {self.name} ({self.zone})>"