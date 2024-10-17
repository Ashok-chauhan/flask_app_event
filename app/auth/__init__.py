from functools import wraps
from flask_login import current_user
from flask import abort
from flask import Blueprint
bp = Blueprint('auth',__name__)
from app.auth import routes




def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                abort(403)  # Forbidden access
            return f(*args, **kwargs)
        return decorated_function
    return decorator
