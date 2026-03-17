from flask import Blueprint, render_template, session

main_bp = Blueprint("main", __name__,)

@main_bp.route("/")

def home():
    session.clear()
    return render_template("home.html")