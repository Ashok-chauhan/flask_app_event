from app.extensions import db
from sqlalchemy.sql import func

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    faculty = db.relationship('Faculty', cascade="all,delete", backref='facultytype')


    def __reper__(self):
        return f'<Events "{self.title}">'
    


class Faculty(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    picture = db.Column(db.String(255))
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
    faculty_type = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Comments "{self.content[:20]}...">'


class Welcome(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    picture = db.Column(db.String(255))
    picture_title = db.Column(db.String(255))
    caption = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f'<Comments "{self.title[:20]}...">'
