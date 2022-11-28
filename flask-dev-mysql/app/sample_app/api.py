import json
from flask import Blueprint

bp = Blueprint("api", __name__, url_prefix="/api/v1")


@bp.route("/example")
def example():
    return json.dumps({
        "message": "hello world"
    })
