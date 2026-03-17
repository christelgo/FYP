import os, uuid
from flask import Blueprint, abort, render_template, request, flash, redirect, url_for
from app.services.order_manager import get_order
# from app.services.bot_engine import send_bot_message
# from app.services.payment_validator import validate_paynow_image
from werkzeug.utils import secure_filename

payment_bp = Blueprint("payment", __name__)

UPLOAD_FOLDER = "app/static/uploads/paynow"
ALLOWED_EXXTENSION = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return(
        "." in filename and 
        filename.rsplit(".",1)[1].lower() in ALLOWED_EXXTENSION
    )

@payment_bp.route("/<order_id>", methods=["GET"])
def paynow(order_id):
    order = get_order(order_id)
    if not order:
        abort(404)
    return render_template("payment.html", order=order)


@payment_bp.route("/upload/<order_id>", methods=["POST"])
def upload_payment(order_id):
    order = get_order(order_id)

    if not order:
        abort(404)
    
    file = request.files.get("paynow_screenshot")

    if not file or file.filename == "":
        flash("Please upload a file")
        return redirect(request.referrer)
    
    if not allowed_file(file.filename):
        flash("Invalid file type")
        return redirect(request.referrer)
    
    filename = secure_filename(file.filename)
    filename = f"{uuid.uuid4()}_{filename}"
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    print("uploadhit", filepath)

    # results = validate_paynow_image(filepath, order)
    # if results["valid"]:
    #     send_bot_message(
    #         order_id= order_id,
    #         message="We've received your Paynow payment and verified your payment"
    #     )
    # else:
    #     send_bot_message(
    #         message="Payment failed"
    #     )

    return render_template("results.html", order=order,image_url= url_for("static", filename=f"uploads/paynow/{filename}"))

