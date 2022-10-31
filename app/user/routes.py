from flask import Blueprint
from app.user.controller import UserRegister, UserAll, UserDetailsId, UserDetailsName


user_api = Blueprint("user_api", __name__)

user_api.add_url_rule("/colaborador/cadastro", view_func=UserRegister.as_view("colaboradorSignup"), methods=["POST"])
user_api.add_url_rule("/colaboradores", view_func=UserAll.as_view("colaboradoresAll"), methods=["GET"])
user_api.add_url_rule("/colaborador/detalhes/<int:user_id>", view_func=UserDetailsId.as_view("colaboradorDetailsId"), methods=["GET", "PUT", "PATCH", "DELETE"])
user_api.add_url_rule("/colaborador/detalhes/<string:user_name>", view_func=UserDetailsName.as_view("colaboradorDetailsName"), methods=["GET"])
