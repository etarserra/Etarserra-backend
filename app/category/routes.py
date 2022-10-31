from flask import Blueprint
from app.category.controller import CategoryAll, CategoryDetails

category_api = Blueprint("category_api", __name__)

category_api.add_url_rule("/category", view_func=CategoryAll.as_view("categoryAll"), methods=["POST", "GET"])
category_api.add_url_rule("/category/<int:category_id>", view_func=CategoryDetails.as_view("categoryDetails"), methods=["GET", "DELETE"])