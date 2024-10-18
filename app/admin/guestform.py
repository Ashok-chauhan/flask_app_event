from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField,FileField, SelectField
from wtforms.validators import InputRequired, length, ValidationError







class GuestForm(FlaskForm):
    title = StringField(validators=[InputRequired()], render_kw={"placeholder":"title"})
    content = TextAreaField(validators=[InputRequired()], render_kw={"placeholder":"Discussion"})
    picture = FileField('picture')
    menu = SelectField(u'Choose an option', choices=[])
    # menu = SelectField(choices=[(context, context) for context in menus], id=menus)
    submit = SubmitField('Create gurest')


