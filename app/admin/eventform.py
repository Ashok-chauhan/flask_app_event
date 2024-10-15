from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TimeField, DateTimeLocalField, FileField
from wtforms.validators import InputRequired, length, ValidationError
#from wtforms.fields import DateTimeField, DateField, TimeField, DateTimeLocalField


class EventForm(FlaskForm):
    date = DateField()
    title = StringField(validators=[InputRequired()], render_kw={"placeholder":"Session name"})
    speaker = StringField(validators=[InputRequired()], render_kw={"placeholder":"Speaker name"})
    speaker_start = TimeField()
    speaker_end = TimeField()
    speaker_file = FileField('speaker_file')

    keynote = StringField(validators=[InputRequired()], render_kw={"placeholder":"Keynote"})
    keynote_start = TimeField(validators=[InputRequired()])
    keynote_end = TimeField(validators=[InputRequired()])
    keynote_file = FileField('keynote_file')

    comments = StringField(validators=[InputRequired()], render_kw={"placeholder":"Discussion"})
    comments_start = TimeField(validators=[InputRequired()])
    comments_end = TimeField(validators=[InputRequired()])
    comments_file = FileField('comments_file')
    breaks = StringField(validators=[InputRequired()], render_kw={"placeholder":"Break"})
    breaks_start = TimeField(validators=[InputRequired()])
    breaks_end = TimeField(validators=[InputRequired()])

    date_time = DateTimeLocalField()
    date_field = DateField()
    time_field = TimeField()
    submit = SubmitField("Create programe")



