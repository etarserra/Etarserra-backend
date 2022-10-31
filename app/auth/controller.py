from datetime import timedelta
from flask import request, render_template
from flask.views import MethodView
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from random import randint
from app.user.models import User
from app.auth.schemas import LoginSchema, NewPasswordSchema
from app.user.schemas import UserSchema
from app.extensions import mail
from app.config import Config
from flask_mail import Message
from marshmallow.exceptions import ValidationError



# /login
class UserLogin(MethodView):

    ''' Usuario faz login no site '''
    def post(self):
        schema = LoginSchema()
        try:
            data = schema.load(request.json)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400

        user = User.query.filter_by(email=data['email']).first_or_404()

        # Verifica se user existe, se senha correta
        if not user or not user.verify_password(data['password']):
            return {"code_status": "invalid user or wrong password"}, 401
        
        # Cria token baseado em tipo de user
        if user.isAdmin == True:
            access_token = create_access_token(identity=user.id, additional_claims={"isAdmin":True})           
        elif user.isAdmin == False:
            access_token = create_access_token(identity=user.id, additional_claims={"isAdmin":False})
        
        # Cria token refresh
        refresh_token = create_refresh_token(identity=user.id)

        return {
            "user": UserSchema().dump(user), 
            "access_token": access_token,
            "refresh_token": refresh_token,
            "isAdmin": user.isAdmin
            }, 200


# /refreshToken
class RefreshToken(MethodView):
    """ Retorna novo access token """
    def get(self):
        #current_user_id = get_jwt_identity()
        return {"access_token": create_access_token(identity=current_user_id)}, 200


# /esquecisenha
class UserPasswordResetEmail(MethodView):

    """ Envia email com pin de trocar de senha """
    def post(self):
        schema = LoginSchema(exclude=['password'])
        try:
            data = schema.load(request.json)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400

        user = User.query.filter_by(email=data['email']).first_or_404()

        verificationPin = str(randint(100000, 999999))
        user.verificationPin = verificationPin
        user.save()
        
        # Manda email pra colaborador
        msg = Message(
            sender=Config.MAIL_USERNAME,
            recipients=[user.email],
            subject="Mudança de Senha",
            html=render_template("emailPasswordColaborador.html", name=user.name, verificationPin=verificationPin, \
                verificationPinTime=Config.VALID_VERIFICATION_PIN_TIME)
        )
        mail.send(msg)
        
        return {"msg": "email enviado com pin",
                "verificationPin": verificationPin,
        }, 200


# /pinInserido
class PinInput(MethodView):

    """ Recebe pin do usuario e verifica se é valido """
    def post(self):
        schema = NewPasswordSchema(exclude=['password'])
        try:
            data = schema.load(request.json)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400

        user = User.query.filter_by(email=data['email']).first_or_404({"msg": "email não encontrado"})

        if not user or not user.verify_pin(data['verificationPin']):
            return {"code_status": "invalid user or pin"}, 401

        return {"isPinValid": True,
                "id": user.id
        }, 200


# /esquecisenha/novasenha/<int:user_id>
class UserPasswordReset(MethodView):

    """ Usuario trocar de senha com pin """
    def patch(self, user_id):
        schema = NewPasswordSchema(exclude=['verificationPin', 'email'])
        try:
            data = schema.load(request.json)
        except ValidationError as e:
            return {"error": "ValidationError", 
                    "msg": str(e)}, 400

        user = User.query.filter_by(id=user_id).first_or_404()

        # Fake it passes 5 minutes
        user.createdPinTimestamp += timedelta(minutes=Config.VALID_VERIFICATION_PIN_TIME)
        user.password = data['password']
        user.save()

        return {"msg": "senha atualizada"}, 200