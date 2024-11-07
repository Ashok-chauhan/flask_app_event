from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField, TimeField, DateTimeLocalField, FileField, TextAreaField
from wtforms.validators import InputRequired, length, ValidationError, optional
#from wtforms.fields import DateTimeField, DateField, TimeField, DateTimeLocalField


# class EventForm(FlaskForm):
#     date = DateField()
#     title = StringField(validators=[InputRequired()], render_kw={"placeholder":"Session name"})
#     speaker = StringField(validators=[InputRequired()], render_kw={"placeholder":"Speaker name"})
#     speaker_start = TimeField()
#     speaker_end = TimeField()
#     speaker_file = FileField('speaker_file')

#     keynote = StringField(validators=[InputRequired()], render_kw={"placeholder":"Keynote"})
#     keynote_start = TimeField(validators=[InputRequired()])
#     keynote_end = TimeField(validators=[InputRequired()])
#     keynote_file = FileField('keynote_file')

#     comments = StringField(validators=[InputRequired()], render_kw={"placeholder":"Discussion"})
#     comments_start = TimeField(validators=[InputRequired()])
#     comments_end = TimeField(validators=[InputRequired()])
#     comments_file = FileField('comments_file')
#     breaks = StringField(validators=[InputRequired()], render_kw={"placeholder":"Break"})
#     breaks_start = TimeField(validators=[InputRequired()])
#     breaks_end = TimeField(validators=[InputRequired()])

#     date_time = DateTimeLocalField()
#     date_field = DateField()
#     time_field = TimeField()
#     submit = SubmitField("Create programe")


class EventForm(FlaskForm):
    agenda_id = SelectField(u'Choose an option', choices=[])
    date = DateField()
    title = StringField(validators=[InputRequired()], render_kw={"placeholder":"Session name"})
    chairpersons = StringField(render_kw={"placeholder":"Chairpersons"})
    keynote_speaker = StringField(render_kw={"placeholder":"Keynote Speaker name"})
    speaker = StringField(render_kw={"placeholder":"Speaker name"})
    speaker_start = TimeField(validators=[optional()])
    speaker_end = TimeField(validators=[optional()])
    speaker_file = FileField('speaker_file')

    keynote = StringField(render_kw={"placeholder":"Keynote"})
    keynote_start = TimeField(validators=[optional()])
    keynote_end = TimeField(validators=[optional()])
    keynote_file = FileField('keynote_file')

    comments = StringField(render_kw={"placeholder":"Discussion"})
    comments_start = TimeField(validators=[optional()])
    comments_end = TimeField(validators=[optional()])
    comments_file = FileField('comments_file')
    breaks = StringField(render_kw={"placeholder":"Break"})
    breaks_start = TimeField(validators=[optional()])
    breaks_end = TimeField(validators=[optional()])

    breaks2 = StringField(render_kw={"placeholder":"Break 2"})
    breaks2_start = TimeField(validators=[optional()])
    breaks2_end = TimeField(validators=[optional()])

    open_house = StringField(render_kw={"placeholder":"Open house"})
    open_house_start = TimeField(validators=[optional()])
    open_house_end = TimeField(validators=[optional()])

    # date_time = DateTimeLocalField()
    # date_field = DateField()
    # time_field = TimeField()
    submit = SubmitField("Create programe")



class WelcomeForm(FlaskForm):
    title = StringField(validators=[InputRequired()], render_kw={"placeholder":"Welcome title"})
    content = TextAreaField(validators=[InputRequired()], render_kw={"placeholder":"Welcome content"})
    picture = FileField('picture')
    picture_title = StringField(validators=[InputRequired()], render_kw={"placeholder":"Picture title"})
    caption = StringField(validators=[InputRequired()], render_kw={"placeholder":"Caption"})
    submit = SubmitField("Submit welcome message")


class VenueForm(FlaskForm):
    title = StringField(validators=[InputRequired()], render_kw={"placeholder":"Venue title"})
    address = StringField(validators=[InputRequired()], render_kw={"placeholder":"Address"})
    content = TextAreaField( render_kw={"placeholder":"Venue"})
    map_link = TextAreaField(render_kw={"placeholder":"Map link"})

    submit = SubmitField("Submit")










