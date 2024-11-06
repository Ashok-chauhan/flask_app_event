from app.extensions import db
from sqlalchemy.sql import func


class Agenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    date = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __reper__(self):
        return f'<Agenda "{self.title}">'


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agenda_id= db.Column(db.Integer, index=True)
    date = db.Column(db.String(100))
    title = db.Column(db.String(255))
    speaker = db.Column(db.String(200))
    speaker_start = db.Column(db.String(100))
    speaker_end = db.Column(db.String(100))
    speaker_file = db.Column(db.String(255))
    keynote = db.Column(db.String(255))
    keynote_start= db.Column(db.String(100))
    keynote_end = db.Column(db.String(100))
    keynote_file = db.Column(db.String(255))
    comments = db.Column(db.String(255))
    comments_start = db.Column(db.String(100))
    comments_end = db.Column(db.String(100))
    comments_file = db.Column(db.String(255))
    breaks = db.Column(db.String(150))
    breaks_start = db.Column(db.String(100))
    breaks_end = db.Column(db.String(100))
    open_house = db.Column(db.String(150))
    open_house_start = db.Column(db.String(100), nullable=True)
    open_house_end = db.Column(db.String(100), nullable=True)
    comment = db.relationship('Comments', cascade="all,delete", backref='events')


    def __reper__(self):
        return f'<Events "{self.title}">'

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __reper__(self):
        return f'<Venue "{self.content}">'

