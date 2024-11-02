from itsdangerous import URLSafeTimedSerializer
from flask import current_app

def generate_token(phone):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(phone, salt='password-reset-salt')

def verify_token(token, expiration=300):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        phone = serializer.loads(
            token,
            salt='password-reset-salt',
            max_age=expiration
        )
    except Exception:
        return None
    return phone

