from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField
from wtforms.validators import InputRequired, length, ValidationError


class CommentForm(FlaskForm):
    content = TextAreaField(validators=[InputRequired()], render_kw={"placeholder":"Discussion"})
    submit = SubmitField("Post discussion")

class PollForm(FlaskForm):
    poll_time = TextAreaField(validators=[InputRequired()], render_kw={"placeholder":"Polling time in seconds"})
    submit = SubmitField("Set polling time in seconds")



