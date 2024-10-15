from app.extensions import db

class Comments(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    events_id = db.Column(db.Integer, db.ForeignKey('events.id'))


    def __repr__(self):
        return f'<Comments "{self.content[:20]}...">'