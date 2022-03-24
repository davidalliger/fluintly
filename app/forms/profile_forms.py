from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, DecimalField
from wtforms.validators import DataRequired, Email, ValidationError, InputRequired, AnyOf, NumberRange
from app.models import User, Profile, Language
from .form_utils import NotEqual, offered_languages, valid_levels, provided_countries, provided_timezones, valid_states, IsInt, RequiredIf, RequiredWhen, InRange, IsValidDate

def validate_display_age(form, field):
    # Checking if display_age is a valid boolean value
    display_age = field.data
    if display_age != True and display_age != False:
        raise ValidationError('Display age on profile must be either true or false.')

class ProfileLanguagesForm(FlaskForm):
    native_language = StringField('Native Language', validators=[
                                                                    DataRequired('Please enter your native language'),
                                                                    AnyOf(offered_languages, message='Must select a language from the options provided')
                                                                ])
    learning_language = StringField('Learning Language', validators=[
                                                                        DataRequired('Please enter your target language'),
                                                                        AnyOf(offered_languages, message='Must select a language from the options provided'),
                                                                        NotEqual('native_language', message='Native language and target language cannot be the same')
                                                                    ])
    proficiency_level = StringField('Proficiency Level', validators=[
                                                                        RequiredIf('learning_language', message='Please enter your proficiency level'),
                                                                        AnyOf(valid_levels, message='Must select a proficiency level from the options provided')
                                                                    ])

class ProfileLocationForm(FlaskForm):
    country = StringField('Country', validators=[
                                                    DataRequired('Please select your country'),
                                                    AnyOf(provided_countries, message='Must select a country from the options provided')
                                                ])
    state = StringField('State', validators=[
                                                RequiredWhen('country', 'United States', message='Please select your state'),
                                                AnyOf(valid_states, message='Must select a state from the options provided')
                                            ])
    timezone = StringField('Time Zone', validators=[
                                                        DataRequired('Please select your time zone'),
                                                        AnyOf(provided_timezones, message='Must select a time zone from the options provided')
                                                    ])

class ProfileAboutForm(FlaskForm):
    month = StringField('Birthday', validators=[
                                                    DataRequired('Please enter your birth month'),
                                                    IsInt('Birth month must be an integer'),
                                                    InRange(min=1, max=12, message='Birth month must be a number between 1 and 12')
                                                ])
    day = StringField('Birthday', validators=[
                                                DataRequired('Please enter your birth date'),
                                                IsInt('Birth date must be an integer'),
                                                IsValidDate('month', message='Please select a valid date')
                                            ])
    year = StringField('Birthday', validators=[
                                                DataRequired('Please enter your birth year'),
                                                IsInt('Birth year must be an integer')
                                            ])
    display_age = BooleanField('Display Age', validators=[validate_display_age])
    about = StringField('About')

class ProfilePictureForm(FlaskForm):
    img_url = StringField('Image')

class ProfileForm(FlaskForm):
    country = StringField('Country', validators=[DataRequired()])
    state = StringField('State')
    timezone = StringField('Time Zone', validators=[DataRequired()])
    birthday = StringField('Birthday', validators=[DataRequired()])
    display_age = BooleanField('Display Age', validators=[validate_display_age])
    about = StringField('About')
    img_url = StringField('Image')
    user_id = IntegerField('User', validators=[DataRequired()])
