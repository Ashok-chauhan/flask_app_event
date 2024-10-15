from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TimeField, DateTimeLocalField
from wtforms.validators import InputRequired, length, ValidationError
#from wtforms.fields import DateTimeField, DateField, TimeField, DateTimeLocalField

class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired()], render_kw={"placeholder":"Email"})
    f_name = StringField(validators=[InputRequired()], render_kw={"placeholder":"First naame"})
    l_name = StringField(validators=[InputRequired()], render_kw={"placeholder":"Last name"})
    phone = StringField(validators=[InputRequired()], render_kw={"placeholder":"Phone number"})

    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder":"Password"})
    # date_time = DateTimeLocalField()
    # date_field = DateField()
    # time_field = TimeField()
    submit = SubmitField("Rgister")


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired()], render_kw={"placeholder":"Email"})
    #name = StringField(validators=[InputRequired()], render_kw={"placeholder":"Name"})
    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder":"Password"})
    submit = SubmitField("Login")

