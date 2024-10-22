from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TimeField, DateTimeLocalField, FileField
from wtforms.validators import InputRequired, length, ValidationError
#from wtforms.fields import DateTimeField, DateField, TimeField, DateTimeLocalField


class UploadForm(FlaskForm):
   
    speaker_file = FileField('speaker_file')

    submit = SubmitField("Create programe")



