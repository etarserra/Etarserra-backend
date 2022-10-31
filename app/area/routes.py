from flask import Blueprint
from app.area.controller import AreaAll, AreaDetails

area_api = Blueprint("area_api", __name__)

area_api.add_url_rule("/area", view_func=AreaAll.as_view("areaAll"), methods=["POST", "GET"])
area_api.add_url_rule("/area/<int:area_id>", view_func=AreaDetails.as_view("areaDetails"), methods=["GET", "DELETE"])