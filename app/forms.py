# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SelectField, SubmitField, TextAreaField, DateField
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
        self.role_id.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]

class StudentProfileForm(FlaskForm):
    age = IntegerField('Age')
    grade = StringField('Grade')
    address = StringField('Address')
    parent_guardian = StringField('Parent/Guardian')
    demographic_info = TextAreaField('Demographic Information')
    discipline_records = TextAreaField('Discipline Records')
    gender_id = SelectField('Gender', coerce=int)
    racial_category_id = SelectField('Racial Category', coerce=int)
    ethnic_background_id = SelectField('Ethnic Background', coerce=int)
    country_id = SelectField('Country of Origin', coerce=int)
    date_of_birth = DateField('Date of Birth')
    place_of_birth = StringField('Place of Birth')
    pronouns = SelectField('Pronouns', choices=[('he/him', 'He/Him'), ('she/her', 'She/Her'), ('they/them', 'They/Them')])
    phone_number = StringField('Phone Number')
    email = StringField('Email')
    emergency_contacts = TextAreaField('Emergency Contacts')
    siblings = TextAreaField('Siblings')
    family_structure = SelectField('Family Structure', choices=[('two-parent', 'Two-Parent'), ('single-parent', 'Single-Parent'), ('foster care', 'Foster Care')])
    custodial_arrangements = TextAreaField('Custodial Arrangements')
    hispanic_latino_origin = BooleanField('Hispanic/Latino Origin')
    primary_language = StringField('Primary Language Spoken at Home')
    other_languages = StringField('Other Languages Spoken')
    english_proficiency = StringField('English Language Proficiency Level')
    esl_ell_status = BooleanField('ESL/ELL Status')
    citizenship_status = StringField('Citizenship Status')
    immigration_status = StringField('Immigration Status')
    date_of_entry_us = DateField('Date of Entry into the US')
    free_reduced_lunch_eligibility = BooleanField('Free/Reduced Lunch Eligibility')
    family_income_bracket = SelectField('Family Income Bracket', choices=[('low', 'Low'), ('middle', 'Middle'), ('high', 'High')])
    parent_education_level = StringField('Parent/Guardian Education Level')
    parent_occupation = StringField('Parent/Guardian Occupation')
    current_grade_level = SelectField('Current Grade Level', choices=[('K', 'Kindergarten'), ('1', '1st Grade'), ('2', '2nd Grade'), ('3', '3rd Grade'), ('4', '4th Grade'), ('5', '5th Grade'), ('6', '6th Grade'), ('7', '7th Grade'), ('8', '8th Grade'), ('9', '9th Grade'), ('10', '10th Grade'), ('11', '11th Grade'), ('12', '12th Grade')])
    previous_schools = TextAreaField('Previous Schools Attended')
    date_of_entry_school_system = DateField('Date of Entry into the School System')
    projected_graduation_year = DateField('Projected Graduation Year')
    iep_status = BooleanField('IEP Status')
    plan_504_status = BooleanField('504 Plan Status')
    gifted_talented_program = BooleanField('Gifted and Talented Program Participation')
    transportation = StringField('Transportation to/from School')
    bus_route_number = StringField('Bus Route Number')
    sports_team_participation = TextAreaField('Sports Team Participation')
    club_memberships = TextAreaField('Club Memberships')
    after_school_program = TextAreaField('After-School Program Enrollment')
    internet_access = BooleanField('Internet Access at Home')
    device_ownership = StringField('Device Ownership/Access')
    active_duty_military_parent = BooleanField('Active Duty Military Parent/Guardian')
    veteran_status_parent = BooleanField('Veteran Status of Parent/Guardian')
    homeless_status = BooleanField('Homeless Status')
    migrant_education_program = BooleanField('Participation in Migrant Education Program')
    foster_care_involvement = BooleanField('Involvement with Foster Care System')
    tribe_membership = BooleanField('Membership in Federally Recognized Tribe')
    religious_affiliation = StringField('Religious Affiliation')
    church_affiliation = StringField('Church Affiliation')
    school_assigned_id = StringField('School-Assigned ID')
    state_assigned_id = StringField('State-Assigned ID')
    national_id = StringField('National ID')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)
        self.gender_id.choices = [(gender.id, gender.name) for gender in Gender.query.order_by(Gender.name).all()]
        self.racial_category_id.choices = [(category.id, category.name) for category in RacialCategory.query.order_by(RacialCategory.name).all()]
        self.ethnic_background_id.choices = [(background.id, background.name) for background in EthnicBackground.query.order_by(EthnicBackground.name).all()]
        self.country_id.choices = [(country.id, country.name) for country in Country.query.order_by(Country.name).all()]

class ParentProfileForm(FlaskForm):
    address = StringField('Address')
    phone_number = StringField('Phone Number')
    submit = SubmitField('Submit')

class TeacherProfileForm(FlaskForm):
    subject = StringField('Subject')
    address = StringField('Address')
    phone_number = StringField('Phone Number')
    submit = SubmitField('Submit')

class UserTypeForm(FlaskForm):
    role_id = SelectField('Role', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Next')

    def __init__(self, *args, **kwargs):
        super(UserTypeForm, self).__init__(*args, **kwargs)
        self.role_id.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
