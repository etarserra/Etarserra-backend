from flask import Blueprint
from app.auth.controller import UserLogin, UserPasswordResetEmail, UserPasswordReset, RefreshToken, PinInput


auth_api = Blueprint("auth_api", __name__)

auth_api.add_url_rule("/login", view_func=UserLogin.as_view("generalUserLogin"), methods=["POST"])
auth_api.add_url_rule("/pinInserido", view_func=PinInput.as_view("pinInput"), methods=["POST"])
auth_api.add_url_rule("/esquecisenha", view_func=UserPasswordResetEmail.as_view("passwordResetEmailUser"), methods=["POST"])
auth_api.add_url_rule("/esquecisenha/novasenha/<int:user_id>", view_func=UserPasswordReset.as_view("passwordResetUser"), methods=["PATCH"])
auth_api.add_url_rule("/refreshToken", view_func=RefreshToken.as_view("refreshToken"), methods=["GET"])