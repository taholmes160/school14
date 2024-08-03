# app/forms.py
    
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.models import Role

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
    age = IntegerField('Age')
    grade = StringField('Grade', validators=[Length(max=10)])
    gender_id = SelectField('Gender', coerce=int)
    racial_category_id = SelectField('Racial Category', coerce=int)
    ethnic_background_id = SelectField('Ethnic Background', coerce=int)
    country_id = SelectField('Country', coerce=int)
    pronouns = StringField('Pronouns', validators=[Length(max=50)])
    family_structure = StringField('Family Structure', validators=[Length(max=50)])
    custodial_arrangements = TextAreaField('Custodial Arrangements')
    hispanic_latino_origin = BooleanField('Hispanic/Latino Origin')
    primary_language = StringField('Primary Language', validators=[Length(max=50)])
    other_languages = StringField('Other Languages', validators=[Length(max=50)])
    english_proficiency = StringField('English Proficiency', validators=[Length(max=50)])
    esl_ell_status = BooleanField('ESL/ELL Status')
    citizenship_status = StringField('Citizenship Status', validators=[Length(max=50)])
    immigration_status = StringField('Immigration Status', validators=[Length(max=50)])
    free_reduced_lunch_eligibility = BooleanField('Free/Reduced Lunch Eligibility')
    family_income_bracket = StringField('Family Income Bracket', validators=[Length(max=50)])
    parent_education_level = StringField('Parent Education Level', validators=[Length(max=50)])
    parent_occupation = StringField('Parent Occupation', validators=[Length(max=50)])
    current_grade_level = StringField('Current Grade Level', validators=[Length(max=10)])
    projected_graduation_year = DateField('Projected Graduation Year', format='%Y-%m-%d')
    iep_status = BooleanField('IEP Status')
    plan_504_status = BooleanField('504 Plan Status')
    gifted_talented_program = BooleanField('Gifted/Talented Program')
    transportation = StringField('Transportation', validators=[Length(max=50)])
    bus_route_number = StringField('Bus Route Number', validators=[Length(max=50)])
    after_school_program = TextAreaField('After School Program')
    internet_access = BooleanField('Internet Access')
    device_ownership = StringField('Device Ownership', validators=[Length(max=50)])
    active_duty_military_parent = BooleanField('Active Duty Military Parent')
    veteran_status_parent = BooleanField('Veteran Status Parent')
    homeless_status = BooleanField('Homeless Status')
    migrant_education_program = BooleanField('Migrant Education Program')
    foster_care_involvement = BooleanField('Foster Care Involvement')
    tribe_membership = BooleanField('Tribe Membership')
    religious_affiliation = StringField('Religious Affiliation', validators=[Length(max=50)])
    church_affiliation = StringField('Church Affiliation', validators=[Length(max=50)])
    submit = SubmitField('Update Selected Users')

    def __init__(self, *args, **kwargs):
        super(BatchUpdateForm, self).__init__(*args, **kwargs)
        self.gender_id.choices = [(g.id, g.name) for g in Gender.query.all()]
        self.racial_category_id.choices = [(r.id, r.name) for r in RacialCategory.query.all()]
        self.ethnic_background_id.choices = [(e.id, e.name) for e in EthnicBackground.query.all()]
        self.country_id.choices = [(c.id, c.name) for c in Country.query.all()]
