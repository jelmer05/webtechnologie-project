from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField, validators
from wtforms.validators import DataRequired,NumberRange, Email, EqualTo  
from wtforms import ValidationError
from webtech.models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm',    message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Leg vast!')

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

class FilterWeekForm(FlaskForm):
    weeknummer = IntegerField('weeknummer', validators=[DataRequired(), NumberRange(min=1, max=52) ])
    submit = SubmitField('Filter')
    
