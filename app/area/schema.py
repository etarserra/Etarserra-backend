from app.extensions import ma
from app.area.model import Area


class AreaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Area
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    name = ma.String()
