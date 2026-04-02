from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, validators, DateField 
from wtforms.validators import DataRequired, NumberRange, Email, EqualTo  
from wtforms import ValidationError
from wtforms.widgets import WeekInput
from webtech.models import User

# --- Custom Field for Week Selection ---

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Registreer')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("dit e-mailadres staat al geregistreerd")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("username is al in gebruik")

class LoginFrom(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Inloggen')

# --- Updated Filter Form ---
class FilterWeekForm(FlaskForm):
    # Use our new WeekField here
    weeknummer = IntegerField('Weeknummer', validators=[DataRequired()]) 
    submit = SubmitField('Filter')
