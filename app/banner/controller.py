from flask import request, abort, make_response, jsonify
from flask.views import MethodView
from app.banner.models import Banner
from app.banner.schemas import BannerSchema
from app.extensions import db
from sqlalchemy import exc

# /banner
class BannerAll(MethodView):
    
    ''' Cadastra um novo banner no banco de dados '''
    def post(self):
        schema = BannerSchema()
        dados = request.json
        
        banner = schema.load(dados)
        db.session.add(banner)
        
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(make_response(jsonify({'errors':str(err.orig)},400)))

        return schema.dump(banner), 201


    ''' Pega um banner do banco de dados '''
    def get(self):
        schema = BannerSchema(many = True)
        return jsonify(schema.dump(Banner.query.all())),200



# /banner/<int:id>
class BannerDetails(MethodView):

    ''' Atualiza dados de um banner no banco de dados '''
    def patch(self, id):
        banner = Banner.query.get_or_404(id)
        schema = BannerSchema()
        dados = request.json
        banner = schema.load(dados, instance=banner, partial = True)

        db.session.add(banner)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(banner),200
    

    ''' Pega um banner do banco de dados '''
    def get(self, id):
        schema = BannerSchema()
        banner = Banner.query.filter_by(id=id).first_or_404()

        return schema.dump(banner), 200
    
    def delete(self, id):
        banner = Banner.query.get_or_404(id)
        db.session.delete(banner)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(make_response(jsonify({'errors':str(err.orig)},400)))
        return {"msg":"Banner deletado!"},200