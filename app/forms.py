# app/forms.py
    
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField, IntegerField, BooleanField, TextAreaField, DateField, SelectMultipleField, widgets, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.models import Role, Gender, RacialCategory, EthnicBackground, Country

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=128)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

      
# app/forms.py
        
class UserForm(FlaskForm):
    user_type_prefix = HiddenField('User Type Prefix')
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=80)], render_kw={'readonly': True})
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)], render_kw={'readonly': True})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=128)], render_kw={'readonly': True})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], render_kw={'readonly': True})
    first_name = StringField('First Name', validators=[Length(max=80)])
    last_name = StringField('Last Name', validators=[Length(max=80)])
    role_id = SelectField('Role', coerce=int)
    is_active = BooleanField('Is Active', default=True)
    is_verified = BooleanField('Is Verified', default=False)
    is_admin = BooleanField('Is Admin', default=False)
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.role_id.choices = [(role.id, role.name) for role in Role.query.all()]

class UserTypeForm(FlaskForm):
    role_id = SelectField('Role', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Next')

    def __init__(self, *args, **kwargs):
        super(UserTypeForm, self).__init__(*args, **kwargs)
        self.role_id.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]


class BatchUpdateForm(FlaskForm):
    # Add a new field to set the grade for the batch update
    set_grade = StringField('Set Grade to', validators=[Length(max=10)])
    # Add a new field to set the age for the batch update
    set_age = IntegerField('Set Age to')
    submit = SubmitField('Update Selected Users')

class AdvancedSearchForm(FlaskForm):
    filter_field = SelectField('Filter By', choices=[('grade', 'Grade'), ('ethnic_origin', 'Ethnic Origin')], validators=[DataRequired()])
    filter_value = StringField('Filter Value', validators=[DataRequired()])
    submit = SubmitField('Filter')

    def __init__(self, *args, **kwargs):
        super(AdvancedSearchForm, self).__init__(*args, **kwargs)
        # Remove the initialization of ethnic_origin since it's no longer needed

class UserProfileForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    submit = SubmitField('Update')