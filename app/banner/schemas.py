from app.extensions import ma
from app.banner.models import Banner

class BannerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Banner
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    media_path = ma.String()
    banner_name = ma.String()