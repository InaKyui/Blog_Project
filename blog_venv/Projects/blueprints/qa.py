from flask import Blueprint

bp = Blueprint(name="qa", import_name=__name__,  url_prefix="/")

@bp.route("/")
def index():
    return "Hello"