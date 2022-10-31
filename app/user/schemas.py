from app.extensions import ma
from app.user.models import User
from flask import abort
from marshmallow import pre_load
from app.config import Config


class UserSchemaPatch(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    name = ma.String()
    email = ma.Email(required=True)
    password = ma.String(required=True, load_only=True)
    isAdmin = ma.Boolean(load_only=True)



class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    name = ma.String()
    email = ma.Email(required=True)
    password = ma.String(required=True, load_only=True)
    isAdmin = ma.Boolean()


    # Verifica se senha e string / se formato aceitavel pra senha
    @pre_load(pass_many=True)
    def validations(self, data, **kwargs):
        password = data.get('password')
        isAdmin = data.get('isAdmin')

        # Verifica se isAdmin é booleano
        if type(isAdmin) != bool:
            abort(400, {"msg": "tipo de usuario errado"})

        # Verifica se senha e string
        if type(password) != str:
            abort(400, {"msg": "Senha com tipo errado"})
        
        # Reduz espacos em branco
        password = password.strip()

        # Espaco em branco
        if password in Config.possiblePasswordErrors:
            abort(400, {"msg": "Senha nao pode ser espaco em branco"})

        # Tamanho senha
        if len(password) < Config.MINIMUM_PASWORD_LENGHT:
            abort(400, {"msg": f"Senha deve possuir no minimo {Config.MINIMUM_PASWORD_LENGHT} caracteres"})
        
        return data
