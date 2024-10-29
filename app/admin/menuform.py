from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class MenuForm(FlaskForm):
    title = StringField(validators=[InputRequired()], render_kw={"placeholder":"title"})
    submit = SubmitField('Submit')
