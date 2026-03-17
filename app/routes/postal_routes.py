from flask import Blueprint, request, jsonify
from app.models.outlet import Outlet
from app.services.location_manager import zone_from_postal

MOCK_OUTLETS = [
    {"id": 1, "name": "Jurong Outlet", "address": "Jurong East", "zone": "West"},
    {"id": 2, "name": "Bugis Outlet", "address": "Bugis", "zone": "Central"},
    {"id": 3, "name": "Tampines Outlet", "address": "Tampines", "zone": "East"},
]


postal_bp = Blueprint("postal_bp", __name__, )
@postal_bp.route("/suggest", methods=["GET"])
def suggest_postal_zone():
    postal_code = request.args.get("postal", "").strip()
    zone = zone_from_postal(postal_code)

    if not zone:
        return jsonify({
            "ok": False,
            "message": "Invalid Singapore postal code"
        }), 400
    outlets = [ o for o in MOCK_OUTLETS if o["zone"] == zone]

    return jsonify({
            "ok": True,
            "postal": postal_code,
            "zone": zone,
            "outlets":outlets
            
        })