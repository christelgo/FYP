from flask import Blueprint, render_template, request, session,redirect, url_for
from app.models.menu_items import MenuItem
from app.services.menu_manager import MENU, prepare_menu

menu_bp = Blueprint("menu", __name__,)

@menu_bp.route("/test")
def test_menu():
    return "MENU ROUTES WORK"

@menu_bp.route("/")
def show_catalouge():
    order_type = request.args.get("type")
    session["order_type"] = order_type
    return render_template("catalouge.html", order_type = order_type) 

@menu_bp.route("/set-order-type/<type>")
def set_order_type(type):
    session["order_type"] = type
    return redirect(url_for("order_bp.personal_info"))


@menu_bp.route("/<menu_type>/<category>")
def show_menu(menu_type, category):
    try:
        items = MENU["categories"][menu_type][category]
        items = prepare_menu(items)
        
    except KeyError:
        return "Menu not found"
    
    ala_first = next(iter(MENU["categories"]["ala_carte"]))
    bento_first = next(iter(MENU["categories"]["Bento_Sets"]))

    return render_template(
        "menu_items.html",
        items = items,
        menu_type = menu_type,
        category = category,
        MENU=MENU,
        set_customisations = MENU["set_customisations"]
    )
