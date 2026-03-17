from flask import Blueprint, render_template, request, session,redirect, url_for
from app.models.menu_items import MenuItem
from app.services.menu_manager import MENU, prepare_menu

menu_bp = Blueprint("menu", __name__,)

@menu_bp.route("/test")
def test_menu():
    return "MENU ROUTES WORK"

@menu_bp.route("/catalouge")
def show_catalouge():
    order_type = session.get("order_type")
    zone = session.get("zone")

    if not order_type or not zone:
        return redirect(url_for("order_bp.personal_info"))
        
    if order_type =="pickup" and not session.get("outlet_id"):
        return redirect(url_for("order_bp.personal_info"))
    
    return render_template("catalouge.html", order_type = order_type, zone = zone, outlet_name = session.get("outlet_name")) 

@menu_bp.route("/set-order-type", methods=["POST"])
def set_order_type():
    order_type = request.form.get("order_type")
    session["order_type"] = order_type
    return redirect(url_for("order_bp.personal_info"))


@menu_bp.route("/<menu_type>/<category>")
def show_menu(menu_type, category):
    order_type = session.get("order_type")
    zone = session.get("zone")

    if not order_type or not zone:
        return redirect(url_for("order_bp.personal_info"))
    
    try:
        items = MENU["categories"][menu_type][category]
        items = prepare_menu(items)
        
    except KeyError:
        return "Menu not found"

    return render_template(
        "menu_items.html",
        items = items,
        menu_type = menu_type,
        category = category,
        order_type=order_type,
        zone=zone,
        MENU=MENU,
        set_customisations = MENU.get("set_customisations", {})
    )

