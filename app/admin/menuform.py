from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import InputRequired


class MenuForm(FlaskForm):
    title = StringField(validators=[InputRequired()], render_kw={"placeholder":"title"})
    submit = SubmitField('Submit')

class AgendaForm(FlaskForm):
    title = StringField(validators=[InputRequired()], render_kw={"placeholder ":"title"})
    date = DateField()
    submit = SubmitField('Submit')
    
