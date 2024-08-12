# app/forms.py
    
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField, IntegerField, TextAreaField, DateField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.models import Role, Gender, RacialCategory, EthnicBackground, Country

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=128)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=128)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
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

class UserProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=80)])
    email = StringField('Email', validators=[DataRequired(), Length(max=120)])
    first_name = StringField('First Name', validators=[Length(max=80)])
    last_name = StringField('Last Name', validators=[Length(max=80)])
    age = IntegerField('Age')
    grade = StringField('Grade', validators=[Length(max=80)])
    address = StringField('Address', validators=[Length(max=120)])
    parent_guardian = StringField('Parent/Guardian', validators=[Length(max=120)])
    demographic_info = TextAreaField('Demographic Info')
    discipline_records = TextAreaField('Discipline Records')
    subject = StringField('Subject', validators=[Length(max=80)])
    phone_number = StringField('Phone Number', validators=[Length(max=20)])
    submit = SubmitField('Update Profile')

class BatchUpdateForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired()])
    grade = StringField('Grade', validators=[Length(max=10)])
    submit = SubmitField('Update Selected Users')
    select_grade = SelectMultipleField('Select Grade', choices=[('NULL', 'No Grade')] + [(str(i), f'{i}th') for i in range(1, 13)], option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=False))
    # Add a new field to set the grade for the batch update
    set_grade = StringField('Set Grade to', validators=[Length(max=10)])
    # Add a new field to set the age for the batch update
    set_age = IntegerField('Set Age to')
    submit = SubmitField('Update Selected Users')

class AdvancedSearchForm(FlaskForm):
    grade = StringField('Grade', validators=[Length(max=80)])
    ethnic_origin = SelectField('Ethnic Origin', coerce=int)
    search = SubmitField('Search')

    def __init__(self, *args, **kwargs):
        super(AdvancedSearchForm, self).__init__(*args, **kwargs)
        self.ethnic_origin.choices = [(0, 'Any')] + [(ethnic.id, ethnic.name) for ethnic in EthnicBackground.query.all()]