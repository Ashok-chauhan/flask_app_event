from app.extensions import db
from flask_login import UserMixin

from sqlalchemy.sql import func


class Users(UserMixin, db.Model):
    id= db.Column(db.Integer, primary_key=True )
    email = db.Column(db.String(150), nullable=True)
    password = db.Column(db.String(255))
    f_name = db.Column(db.String(150))
    l_name = db.Column(db.String(150))
    phone = db.Column(db.String(150), unique=True , nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


    def __repr__(self):
        return f'<Users "{self.email}">'