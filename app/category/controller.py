from flask import jsonify, request
from flask.views import MethodView
from app.category.model import Category
from app.category.schema import CategorySchema
from app.category.services import category_services
from marshmallow.exceptions import ValidationError

# /category
class CategoryAll(MethodView):

    """ Mostra todas categorias em ordem """
    def get(self):
        schema = CategorySchema(many=True)
        categories = Category.query.order_by(Category.name).all()

        return jsonify(schema.dump(categories)), 200
    
    """ Cria nova categoria """
    def post(self):
        schema = CategorySchema()
        try:
            category = category_services.create(request.json, schema)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400
            
        return schema.dump(category), 200



#/category/<int:category_id>
class CategoryDetails(MethodView):

    """ Pega categoria especifica """
    def get(self, category_id):
        schema = CategorySchema()
        category = Category.query.filter_by(id=category_id).first_or_404()

        return schema.dump(category), 200


    ''' Deleta categoria '''
    def delete(self, category_id):
        category_services.delete_by_id(category_id)

        return {"msg": "category has been deleted"}, 200