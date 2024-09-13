from flask_wtf import FlaskForm
from wtforms import DateField, StringField, PasswordField, BooleanField, SelectField, SubmitField, IntegerField, HiddenField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from app.models import Role, Gender, GenderIdentity, Pronoun, FamilyStructure, CustodialArrangement, RacialCategory, EthnicBackground, Language, CitizenshipStatus, Country, ImmigrationStatus, FamilyIncomeBracket, ParentEducationLevel, ParentOccupation, CurrentGradeLevel, IEPStatus, BusRouteDistrict, BusRouteNumber, SportsTeamParticipation, ClubMembership, InternetAccess, DeviceOwnership, ActiveDutyParent, VeteranStatusParent, HomelessStatus, MigrantEducationProgram, FosterCareInvolvement, TribalAffiliation, ReligiousAffiliation, State, ParentLifeStatus, EnrollmentStatus, ExitWithdrawalStatus, ExitWithdrawalType, NonPromotionReason, DisabilityType

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
    grade = QuerySelectField('Grade', query_factory=lambda: CurrentGradeLevel.query.all(), get_label='name', allow_blank=True)
    preferred_name = StringField('Preferred Name', validators=[Length(max=80)])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    place_of_birth = StringField('Place of Birth', validators=[Length(max=255)])
    gender = QuerySelectField('Gender', query_factory=lambda: Gender.query.all(), get_label='name', allow_blank=True)
    gender_identity = QuerySelectField('Gender Identity', query_factory=lambda: GenderIdentity.query.all(), get_label='name', allow_blank=True)
    pronouns = QuerySelectField('Pronouns', query_factory=lambda: Pronoun.query.all(), get_label='name', allow_blank=True)
    home_address = StringField('Home Address', validators=[Length(max=255)])
    phone_numbers = StringField('Phone Numbers', validators=[Length(max=255)])
    email_address = StringField('Email Address', validators=[Email(), Length(max=120)])
    family_structure = QuerySelectField('Family Structure', query_factory=lambda: FamilyStructure.query.all(), get_label='name', allow_blank=True)
    custodial_arrangement = QuerySelectField('Custodial Arrangement', query_factory=lambda: CustodialArrangement.query.all(), get_label='name', allow_blank=True)
    racial_category = QuerySelectField('Racial Category', query_factory=lambda: RacialCategory.query.all(), get_label='name', allow_blank=True)
    ethnic_background = QuerySelectField('Ethnic Background', query_factory=lambda: EthnicBackground.query.all(), get_label='name', allow_blank=True)
    primary_language = QuerySelectField('Primary Language', query_factory=lambda: Language.query.all(), get_label='name', allow_blank=True)
    other_language = QuerySelectField('Other Language', query_factory=lambda: Language.query.all(), get_label='name', allow_blank=True)
    citizenship_status = QuerySelectField('Citizenship Status', query_factory=lambda: CitizenshipStatus.query.all(), get_label='name', allow_blank=True)
    country = QuerySelectField('Country', query_factory=lambda: Country.query.all(), get_label='name', allow_blank=True)
    immigration_status = QuerySelectField('Immigration Status', query_factory=lambda: ImmigrationStatus.query.all(), get_label='name', allow_blank=True)
    family_income_bracket = QuerySelectField('Family Income Bracket', query_factory=lambda: FamilyIncomeBracket.query.all(), get_label='name', allow_blank=True)
    parent_education_level = QuerySelectField('Parent Education Level', query_factory=lambda: ParentEducationLevel.query.all(), get_label='name', allow_blank=True)
    parent_occupation = QuerySelectField('Parent Occupation', query_factory=lambda: ParentOccupation.query.all(), get_label='name', allow_blank=True)
    iep_status = QuerySelectField('IEP Status', query_factory=lambda: IEPStatus.query.all(), get_label='name', allow_blank=True)
    bus_route_district = QuerySelectField('Bus Route District', query_factory=lambda: BusRouteDistrict.query.all(), get_label='name', allow_blank=True)
    bus_route_number = QuerySelectField('Bus Route Number', query_factory=lambda: BusRouteNumber.query.all(), get_label='name', allow_blank=True)
    sports_team_participation = QuerySelectField('Sports Team Participation', query_factory=lambda: SportsTeamParticipation.query.all(), get_label='name', allow_blank=True)
    club_membership = QuerySelectField('Club Membership', query_factory=lambda: ClubMembership.query.all(), get_label='name', allow_blank=True)
    internet_access = QuerySelectField('Internet Access', query_factory=lambda: InternetAccess.query.all(), get_label='name', allow_blank=True)
    device_ownership = QuerySelectField('Device Ownership', query_factory=lambda: DeviceOwnership.query.all(), get_label='name', allow_blank=True)
    active_duty_parent = QuerySelectField('Active Duty Parent', query_factory=lambda: ActiveDutyParent.query.all(), get_label='name', allow_blank=True)
    veteran_status_parent = QuerySelectField('Veteran Status Parent', query_factory=lambda: VeteranStatusParent.query.all(), get_label='name', allow_blank=True)
    homeless_status = QuerySelectField('Homeless Status', query_factory=lambda: HomelessStatus.query.all(), get_label='name', allow_blank=True)
    migrant_education_program = QuerySelectField('Migrant Education Program', query_factory=lambda: MigrantEducationProgram.query.all(), get_label='name', allow_blank=True)
    foster_care_involvement = QuerySelectField('Foster Care Involvement', query_factory=lambda: FosterCareInvolvement.query.all(), get_label='name', allow_blank=True)
    tribe_membership = QuerySelectField('Tribal Membership', query_factory=lambda: TribalAffiliation.query.all(), get_label='name', allow_blank=True)
    religious_affiliation = QuerySelectField('Religious Affiliation', query_factory=lambda: ReligiousAffiliation.query.all(), get_label='name', allow_blank=True)
    state = QuerySelectField('State', query_factory=lambda: State.query.all(), get_label='name', allow_blank=True)
    parent_life_status = QuerySelectField('Parent Life Status', query_factory=lambda: ParentLifeStatus.query.all(), get_label='name', allow_blank=True)
    enrollment_status = QuerySelectField('Enrollment Status', query_factory=lambda: EnrollmentStatus.query.all(), get_label='name', allow_blank=True)
    exit_withdrawal_status = QuerySelectField('Exit Withdrawal Status', query_factory=lambda: ExitWithdrawalStatus.query.all(), get_label='name', allow_blank=True)
    exit_withdrawal_type = QuerySelectField('Exit Withdrawal Type', query_factory=lambda: ExitWithdrawalType.query.all(), get_label='name', allow_blank=True)
    non_promotion_reason = QuerySelectField('Non Promotion Reason', query_factory=lambda: NonPromotionReason.query.all(), get_label='name', allow_blank=True)
    disability_type_primary = QuerySelectField('Disability Type - Primary', query_factory=lambda: DisabilityType.query.all(), get_label='name', allow_blank=True)
    disability_type_secondary = QuerySelectField('Disability Type - Secondary', query_factory=lambda: DisabilityType.query.all(), get_label='name', allow_blank=True)
    disability_type_tertiary = QuerySelectField('Disability Type - Tertiary', query_factory=lambda: DisabilityType.query.all(), get_label='name', allow_blank=True)
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
