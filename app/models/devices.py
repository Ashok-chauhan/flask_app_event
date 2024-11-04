from app.extensions import db
from sqlalchemy.sql import func

class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), index=True)
    role = db.Column(db.String(6))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    

    def __reper__(self):
        return f'<Events "{self.token}">'