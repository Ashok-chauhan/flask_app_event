from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TimeField, DateTimeLocalField, TextAreaField
from wtforms.validators import InputRequired, length, ValidationError
#from wtforms.fields import DateTimeField, DateField, TimeField, DateTimeLocalField

class PostForm(FlaskForm):
    title = StringField(validators=[InputRequired()], render_kw={"placeholder":"Title"})
    content = TextAreaField(validators=[InputRequired()], render_kw={"placeholder":"Content"})
   
    submit = SubmitField("Submit")
