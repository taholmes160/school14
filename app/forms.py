# app/forms.py
    
from flask_wtf import FlaskForm
from wtforms import DateField, StringField, PasswordField, BooleanField, SelectField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.models import Role

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=128)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

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
    set_grade = StringField('Set Grade to', validators=[Length(max=10)])
    set_age = IntegerField('Set Age to')
    submit = SubmitField('Update Selected Users')

class AdvancedSearchForm(FlaskForm):
    filter_field = SelectField('Filter By', choices=[('grade', 'Grade'), ('ethnic_origin', 'Ethnic Origin')], validators=[DataRequired()])
    filter_value = StringField('Filter Value', validators=[DataRequired()])
    submit = SubmitField('Filter')

    def __init__(self, *args, **kwargs):
        super(AdvancedSearchForm, self).__init__(*args, **kwargs)

class UserProfileForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    preferred_name = StringField('Preferred Name', validators=[Length(max=80)])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    place_of_birth = StringField('Place of Birth', validators=[Length(max=255)])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    gender_identity = SelectField('Gender Identity', choices=[('cisgender', 'Cisgender'), ('transgender', 'Transgender'), ('non_binary', 'Non-binary'), ('other', 'Other')], validators=[Length(max=50)])
    pronouns = SelectField('Pronouns', choices=[('he/him', 'He/Him'), ('she/her', 'She/Her'), ('they/them', 'They/Them'), ('other', 'Other')], validators=[Length(max=50)])
    home_address = StringField('Home Address', validators=[Length(max=255)])
    phone_numbers = StringField('Phone Numbers', validators=[Length(max=255)])
    email_address = StringField('Email Address', validators=[Email(), Length(max=120)])
    submit = SubmitField('Update')

class SelectGradeForm(FlaskForm):
    grade_choices = [
        ('pk4', 'PK4'), ('pk5', 'PK5'), ('kdg', 'KDG'),
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
        ('11', '11'), ('12', '12')
    ]
    grade = SelectField('Grade', choices=grade_choices, validators=[DataRequired()])
    submit = SubmitField('Generate Report')
