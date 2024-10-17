from app.extensions import db

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
    comment = db.relationship('Comments', cascade="all,delete", backref='events')


    def __reper__(self):
        return f'<Events "{self.title}">'
