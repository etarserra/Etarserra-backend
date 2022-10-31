from flask import Blueprint
from app.banner.controller import BannerAll, BannerDetails

banner_api = Blueprint("banner_api", __name__)

banner_api.add_url_rule("/banner", view_func=BannerAll.as_view("allBanner"), methods=["POST", "GET"])
banner_api.add_url_rule("/banner/<int:id>", view_func=BannerDetails.as_view("bannerDetails"), methods=["GET", "PATCH", "DELETE"])