from app.extensions import ma
from app.file.models import File
from app.author.schemas import AuthorSchema
from app.tag.schemas import TagSchema
from app.category.schema import CategorySchema
from app.area.schema import AreaSchema

class FileSchema(ma.SQLAlchemySchema):
    class Meta:
        model = File
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    creationTimeStamp = ma.DateTime(required=False)
    media_path = ma.String()
    type = ma.String()
    click_quantity = ma.Integer()
    title = ma.String()
    year = ma.Integer()
    awarded = ma.String()
    description = ma.String()
    creator_id = ma.Integer()
    authors_associated = ma.Nested(AuthorSchema, only=['name','id'], many=True)
    tags_associated = ma.Nested(TagSchema, only=['name','id'], many=True)
    categories_associated = ma.Nested(CategorySchema, only=['name','id'], many=True)
    areas_associated = ma.Nested(AreaSchema, only=['name','id'], many=True)