from flask import Blueprint, render_template
from app.models.menu_items import MenuItem
from app.services.menu_manager import MENU

menu_bp = Blueprint("menu", __name__,)

@menu_bp.route("/test")
def test_menu():
    return "MENU ROUTES WORK"


@menu_bp.route("/<menu_type>/<category>")
def show_menu(menu_type, category):
    try:
        items = MENU["categories"][menu_type][category]


    except KeyError:
        return "Menu not found"
    
    return render_template(
        "menu_items.html",
        items = items,
        menu_type = menu_type,
        category = category,
        MENU=MENU,
        set_customisations = MENU["set_customisations"]
    )
