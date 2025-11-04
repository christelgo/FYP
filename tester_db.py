from app import create_app, db
from app.config import TestConfig
from app.models.menu_items import MenuItem

app = create_app()
app.config.from_object(TestConfig)

with app.app_context():
    db.drop_all()
    db.create_all()
    tester_menu = [
        MenuItem(name="Chicken Chop", price=12.50, category="Ala Carte"), 
        MenuItem(name="Grilled Salmon", price=18.90, category="Ala Carte"),
        MenuItem(name="Truffle Fries", price=6.50, category="Sides"),
        MenuItem(name="Iced Lemon Tea", price=3.00, category="Drinks"),
        MenuItem(name="Signature Wagyu Burger", price=22.00, category="Chef Recommendation"), ]
    db.session.add_all(tester_menu)
    db.session.commit()

    print("Tester menu database has added successfully")