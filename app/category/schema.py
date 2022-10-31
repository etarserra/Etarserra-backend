from app.extensions import ma
from app.category.model import Category


class CategorySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Category
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    name = ma.String()
