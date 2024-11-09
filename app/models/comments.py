from app.extensions import db
from sqlalchemy.sql import func

# class Comments(db.Model):
#     id= db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text)
#     user_name = db.Column(db.String(255))
#     events_id = db.Column(db.Integer, db.ForeignKey('events.id'))
#     status = db.Column(db.Integer, nullable=False, default=0)
#     created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())



#     def __repr__(self):
#         return f'<Comments "{self.content[:20]}...">'
    


class Questions(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, index=True)
    user_name = db.Column(db.String(255))
    status = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())



    def __repr__(self):
        return f'<Comments "{self.content[:20]}...">'


class Polltime(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    poll_time = db.Column(db.Integer, nullable=False, default=30)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())



    def __repr__(self):
        return f'<Comments "{self.content[:20]}...">'