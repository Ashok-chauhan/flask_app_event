from app.extensions import db
from sqlalchemy.sql import func

class Comments(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_name = db.Column(db.String(255))
    events_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    status = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())



    def __repr__(self):
        return f'<Comments "{self.content[:20]}...">'