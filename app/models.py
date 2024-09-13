from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255))
    permissions = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'<Role {self.name}>'

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(512))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    profile_picture = db.Column(db.String(120))
    bio = db.Column(db.String(500))
    phone_number = db.Column(db.String(20))
    last_login_at = db.Column(db.DateTime)
    login_attempts = db.Column(db.Integer, default=0)
    password_reset_token = db.Column(db.String(120))
    password_reset_expiration = db.Column(db.DateTime)
    language = db.Column(db.String(10))
    timezone = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean, default=False)
    deactivated_at = db.Column(db.DateTime)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.id)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active_user(self):
        return self.is_active

    @property
    def is_anonymous(self):
        return False

    def __repr__(self):
        return f'<User {self.username}>'

class StudentProfile(db.Model):
    __tablename__ = 'student_profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    grade_id = db.Column(db.Integer, db.ForeignKey('current_grade_levels.id'), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    parent_guardian = db.Column(db.String(255), nullable=True)
    demographic_info = db.Column(db.Text, nullable=True)
    discipline_records = db.Column(db.Text, nullable=True)
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'), nullable=True)
    racial_category_id = db.Column(db.Integer, db.ForeignKey('racial_categories.id'), nullable=True)
    ethnic_background_id = db.Column(db.Integer, db.ForeignKey('ethnic_backgrounds.id'), nullable=True)
    device_ownership_id = db.Column(db.Integer, db.ForeignKey('device_ownerships.id'), nullable=True)
    active_duty_parent_id = db.Column(db.Integer, db.ForeignKey('active_duty_parents.id'), nullable=True)
    veteran_status_parent_id = db.Column(db.Integer, db.ForeignKey('veteran_status_parents.id'), nullable=True)
    homeless_status_id = db.Column(db.Integer, db.ForeignKey('homeless_statuses.id'), nullable=True)
    migrant_education_program_id = db.Column(db.Integer, db.ForeignKey('migrant_education_programs.id'), nullable=True)
    foster_care_involvement_id = db.Column(db.Integer, db.ForeignKey('foster_care_involvements.id'), nullable=True)
    tribe_membership_id = db.Column(db.Integer, db.ForeignKey('tribal_affiliations.id'), nullable=True)
    religious_affiliation_id = db.Column(db.Integer, db.ForeignKey('religious_affiliations.id'), nullable=True)
    school_assigned_id = db.Column(db.String(50), nullable=True)
    state_assigned_id = db.Column(db.String(50), nullable=True)
    national_id = db.Column(db.String(50), nullable=True)
    preferred_name = db.Column(db.String(80), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    place_of_birth = db.Column(db.String(255), nullable=True)
    gender_identity_id = db.Column(db.Integer, db.ForeignKey('gender_identities.id'), nullable=True)
    home_address = db.Column(db.String(255), nullable=True)
    phone_numbers = db.Column(db.String(255), nullable=True)
    email_address = db.Column(db.String(120), nullable=True)
    emergency_contacts = db.relationship('EmergencyContact', backref='student_profile', lazy=True)
    parent_guardians = db.relationship('ParentProfile', backref='student_profile', lazy=True)
    user = db.relationship('User', backref=db.backref('student_profile', uselist=False))
    grade = db.relationship('CurrentGradeLevel', backref='student_profiles')

    def __repr__(self):
        return f'<StudentProfile {self.id}>'

class CurrentGradeLevel(db.Model):
    __tablename__ = 'current_grade_levels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f'<CurrentGradeLevel {self.name}>'

class Gender(db.Model):
    __tablename__ = 'genders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Gender {self.name}>'

class GenderIdentity(db.Model):
    __tablename__ = 'gender_identities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<GenderIdentity {self.name}>'

class Pronoun(db.Model):
    __tablename__ = 'pronouns'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Pronoun {self.name}>'

class FamilyStructure(db.Model):
    __tablename__ = 'family_structures'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<FamilyStructure {self.name}>'

class CustodialArrangement(db.Model):
    __tablename__ = 'custodial_arrangements'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<CustodialArrangement {self.name}>'

class RacialCategory(db.Model):
    __tablename__ = 'racial_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<RacialCategory {self.name}>'

class EthnicBackground(db.Model):
    __tablename__ = 'ethnic_backgrounds'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<EthnicBackground {self.name}>'

class Language(db.Model):
    __tablename__ = 'languages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Language {self.name}>'

class CitizenshipStatus(db.Model):
    __tablename__ = 'citizenship_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<CitizenshipStatus {self.name}>'

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Country {self.name}>'

class ImmigrationStatus(db.Model):
    __tablename__ = 'immigration_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<ImmigrationStatus {self.name}>'

class FamilyIncomeBracket(db.Model):
    __tablename__ = 'family_income_brackets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<FamilyIncomeBracket {self.name}>'

class ParentEducationLevel(db.Model):
    __tablename__ = 'parent_education_levels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<ParentEducationLevel {self.name}>'

class ParentOccupation(db.Model):
    __tablename__ = 'parent_occupations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<ParentOccupation {self.name}>'

class IEPStatus(db.Model):
    __tablename__ = 'iep_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<IEPStatus {self.name}>'

class BusRouteDistrict(db.Model):
    __tablename__ = 'bus_route_districts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<BusRouteDistrict {self.name}>'

class BusRouteNumber(db.Model):
    __tablename__ = 'bus_route_numbers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<BusRouteNumber {self.name}>'

class SportsTeamParticipation(db.Model):
    __tablename__ = 'sports_team_participations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<SportsTeamParticipation {self.name}>'

class ClubMembership(db.Model):
    __tablename__ = 'club_memberships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<ClubMembership {self.name}>'

class InternetAccess(db.Model):
    __tablename__ = 'internet_accesses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<InternetAccess {self.name}>'

class DeviceOwnership(db.Model):
    __tablename__ = 'device_ownerships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<DeviceOwnership {self.name}>'

class ActiveDutyParent(db.Model):
    __tablename__ = 'active_duty_parents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<ActiveDutyParent {self.name}>'

class VeteranStatusParent(db.Model):
    __tablename__ = 'veteran_status_parents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<VeteranStatusParent {self.name}>'

class HomelessStatus(db.Model):
    __tablename__ = 'homeless_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<HomelessStatus {self.name}>'

class MigrantEducationProgram(db.Model):
    __tablename__ = 'migrant_education_programs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<MigrantEducationProgram {self.name}>'

class FosterCareInvolvement(db.Model):
    __tablename__ = 'foster_care_involvements'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<FosterCareInvolvement {self.name}>'

class TribalAffiliation(db.Model):
    __tablename__ = 'tribal_affiliations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<TribalAffiliation {self.name}>'

class ReligiousAffiliation(db.Model):
    __tablename__ = 'religious_affiliations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<ReligiousAffiliation {self.name}>'

class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<State {self.name}>'

class ParentLifeStatus(db.Model):
    __tablename__ = 'parent_life_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<ParentLifeStatus {self.name}>'

class EnrollmentStatus(db.Model):
    __tablename__ = 'enrollment_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<EnrollmentStatus {self.name}>'

class ExitWithdrawalStatus(db.Model):
    __tablename__ = 'exit_withdrawal_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<ExitWithdrawalStatus {self.name}>'

class ExitWithdrawalType(db.Model):
    __tablename__ = 'exit_withdrawal_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<ExitWithdrawalType {self.name}>'

class NonPromotionReason(db.Model):
    __tablename__ = 'non_promotion_reasons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<NonPromotionReason {self.name}>'

class DisabilityType(db.Model):
    __tablename__ = 'disability_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<DisabilityType {self.name}>'
