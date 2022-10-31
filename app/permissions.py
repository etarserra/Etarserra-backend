from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.user.services import user_services


# Permissao de usuario
def user_permission(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        if kwargs.get('user_id') != get_jwt_identity():
            return {'error': 'Unauthorized user',
                    'user_id': kwargs.get("user_id"),
                    'jwt': get_jwt_identity()}, 401
        else:
            return func(*args, **kwargs)
    return wrapper


# Permissao de admin
def admin_permission(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        user = user_services.get_by_id(get_jwt_identity())
        if user.user_type != 'admin':
            return {"error": "Unauthorized user"}, 401
        else:
            return func(*args, **kwargs)
    return wrapper
