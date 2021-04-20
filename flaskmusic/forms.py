from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, MultipleFileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, DataRequired


class MusicForm(FlaskForm):
    music = MultipleFileField(
        'music', validators=[DataRequired()])
