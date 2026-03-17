from flask import Blueprint, request, jsonify, render_template, session,json, redirect, url_for, abort
from app.services import order_manager, delivery_service
from app.services.order_manager import create_draft_order, get_order
from app.services.location_manager import zone_from_postal
from app.services.bot_engine import send_bot_message
from app.models.outlet import Outlet

MOCK_OUTLETS = [
    {"id": 1, "name": "Jurong Outlet", "address": "Jurong East", "zone": "West"},
    {"id": 2, "name": "Bugis Outlet", "address": "Bugis", "zone": "Central"},
    {"id": 3, "name": "Tampines Outlet", "address": "Tampines", "zone": "East"},
]

order_bp = Blueprint('order_bp', __name__, )
# testing
@order_bp.route('/', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = order_manager.create_order(data)
    return jsonify({"message": ["Your Order has been created "] ,"order":new_order.to_dict()}),201

#input customer personal details ie. name, date
@order_bp.route("/info", methods = ["GET", "POST"])
def personal_info():
    if request.method == "POST":
        session["customer_name"] = request.form.get("customer_name")
        session["customer_phone"] = request.form.get("customer_phone")

        order_type = session.get("order_type")
    

        if order_type == "delivery":
            session["postal_code"] = request.form.get("postal_code")
            zone = zone_from_postal(session["postal_code"] )

            if not zone:
                return render_template(
                    "personal_info.html",
                    order_type=order_type,
                    outlets=MOCK_OUTLETS
                )
            session["zone"]=zone
            session["address"] = request.form.get("address")

        
        elif order_type == "pickup":
            outlet_id = request.form.get("outlet_id")
            pickup_time = request.form.get("pickup_time")
            session["pickup_time"] = pickup_time
            if not outlet_id:
                return render_template(
                    "personal_info.html",
                    order_type= order_type,
                    outlets = MOCK_OUTLETS
                )

            outlet = next(
                (o for o in MOCK_OUTLETS if o["id"]== int(outlet_id)),
                None
            )
            if not outlet:
                return render_template(
                    "personal_info.html",
                    order_type= order_type,
                    outlets = MOCK_OUTLETS)
            
            session["outlet_id"] = outlet_id
            session['outlet_name'] = outlet["name"]
            session["zone"]=outlet["zone"]

    
        return redirect(url_for("menu.show_catalouge"))
    
    return render_template(
        "personal_info.html",
        order_type = session.get("order_type"),
        outlets = MOCK_OUTLETS
    )

@order_bp.route("/checkout", methods=["POST"])
def checkout():
    raw_cart = request.form.get("cart_data", "")
    if not raw_cart:
        cart= []
    else:
        cart = json.loads(raw_cart)
    order = create_draft_order(
        cart=cart,
        customer_name = session.get("customer_name"),
        customer_phone= session.get("customer_phone"),
        order_type = session.get("order_type"),
        postal_code = session.get("postal_code"),
        zone = session.get("zone"),
        address = session.get("address"),
        outlet_id = session.get("outlet_id"),
        outlet_name = session.get("outlet_name")
        )
    return redirect(url_for("order_bp.order_summary", order_id = order["id"]))

@order_bp.route("/order/<order_id>")
def order_summary(order_id):
    order= get_order(order_id)

    if not order:
        abort(404)
    
    return render_template(
        "order_summary.html",
        order = order
        )

# customer is dead set they want these items and method of recieving
@order_bp.route("/order/<order_id>/confirm", methods= ["POST"])
def confirm_order(order_id):
    order = get_order(order_id)
    if not order:
        abort(404)
    send_bot_message(
        to=order["customer_phone"],
        message= "Thanks! We've reveived your order and are waiting for your payment"
    )

    # order["status"]= "CONFIRMED"
    return redirect(url_for("order_bp.processing", order_id= order_id))

#customer send items to the "kitchen" and is waiting for them to say they received their order
@order_bp.route("/order/<order_id>/processing")
def processing(order_id):
    order = get_order(order_id)

    if order["order_type"] == "delivery":
        quote =delivery_service.get_lalamove_price(order)
        order["delivery_breakdown"] = quote or {"base_fee": 0}
    else:
        
        order["delivery_breakdown"] = {"base_fee": 0}
        
    order["final_total"]= round(order["subtotal"] + order["delivery_fee"],2)

    return render_template("processing.html", order=order)


