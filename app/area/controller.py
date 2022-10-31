from flask import jsonify, request
from flask.views import MethodView
from app.area.model import Area
from app.area.schema import AreaSchema
from app.area.services import area_services
from marshmallow.exceptions import ValidationError

# /area
class AreaAll(MethodView):

    """ Mostra todas areas em ordem """
    def get(self):
        schema = AreaSchema(many=True)
        areas = Area.query.order_by(Area.name).all()

        return jsonify(schema.dump(areas)), 200
    
    """ Cria nova area """
    def post(self):
        schema = AreaSchema()
        try:
            area = area_services.create(request.json, schema)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400
            
        return schema.dump(area), 200



#/area/<int:area_id>
class AreaDetails(MethodView):

    """ Pega area especifica """
    def get(self, area_id):
        schema = AreaSchema()
        area = Area.query.filter_by(id=area_id).first_or_404()

        return schema.dump(area), 200


    ''' Deleta area '''
    def delete(self, area_id):
        area_services.delete_by_id(area_id)

        return {"msg": "area has been deleted"}, 200