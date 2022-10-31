from flask import jsonify, request, render_template
from flask_mail import Message
from app.extensions import mail
from app.config import Config
from flask.views import MethodView
from app.user.models import User
from app.user.schemas import UserSchema, UserSchemaPatch
from app.user.services import user_services
from app.permissions import admin_permission
from marshmallow.exceptions import ValidationError


# /colaborador/cadastro
class UserRegister(MethodView):
    
    ''' Cadastra novo coloborador no banco de dados '''
    #decorators = [admin_permission()]
    def post(self):
        schema = UserSchema()

        try:
            user = user_services.create(request.json, schema)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400

        
        # Manda email pra colaborador
        msg = Message(
            sender=Config.MAIL_USERNAME,
            recipients=[user.email],
            subject="Bem-vindo(a) Colaborador!",
            html=render_template("emailWelcomeColaborador.html", name=user.name)
        )
        mail.send(msg)
        
        return schema.dump(user), 200




# /colaboradores
class UserAll(MethodView):

    ''' Mostra todos colaboradores em ordem'''
    #decorators = [admin_permission()]
    def get(self):
        schema = UserSchema(many=True, exclude=['password'])
        users = User.query.order_by(User.name).all()

        return jsonify(schema.dump(users)), 200




# /colaborador/detalhes/<int:user_id>
class UserDetailsId(MethodView):

    ''' Pega dados de usuario especifico por id '''
    #decorators = [admin_permission()]
    def get(self, user_id):
        schema = UserSchema()
        user = User.query.filter_by(id=user_id).first_or_404()

        return schema.dump(user), 200
    

    ''' Altera informacao parcial do usuario '''
    def patch(self, user_id):
        schema = UserSchemaPatch() 
        try:
            user = user_services.update_by_id(user_id, request.json, schema, partial=True)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400

        return schema.dump(user), 200
    

    ''' Altera informacao total do usuario '''
    def put(self, user_id):
        schema = UserSchemaPatch() 
        try:
            user = user_services.update_by_id(user_id, request.json, schema, partial=False)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400

        return schema.dump(user), 200
    

    ''' Deleta usuario '''
    def delete(self, user_id):
        user_services.delete_by_id(user_id)

        return {"msg": "user has been deleted"}, 200




# /colaborador/detalhes/<string:user_name>
class UserDetailsName(MethodView):

    ''' Pega dados de usuario especifico por nome '''
    #decorators = [admin_permission()]
    def get(self, user_name):
        schema = UserSchema()
        user = User.query.filter_by(name=user_name).first_or_404()

        return schema.dump(user), 200
    
 