# app/models.py

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
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    place_of_birth = db.Column(db.String(255), nullable=True)
    pronoun_id = db.Column(db.Integer, db.ForeignKey('pronouns.id'), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    family_structure_id = db.Column(db.Integer, db.ForeignKey('family_structures.id'), nullable=True)
    custodial_arrangement_id = db.Column(db.Integer, db.ForeignKey('custodial_arrangements.id'), nullable=True)
    hispanic_latino_origin = db.Column(db.Boolean, nullable=True)
    primary_language_id = db.Column(db.Integer, db.ForeignKey('languages.id'), nullable=True)
    other_language_id = db.Column(db.Integer, db.ForeignKey('languages.id'), nullable=True)
    english_proficiency = db.Column(db.String(50), nullable=True)
    esl_ell_status = db.Column(db.Boolean, nullable=True)
    citizenship_status_id = db.Column(db.Integer, db.ForeignKey('citizenship_statuses.id'), nullable=True)
    immigration_status_id = db.Column(db.Integer, db.ForeignKey('immigration_statuses.id'), nullable=True)
    date_of_entry_us = db.Column(db.Date, nullable=True)
    free_reduced_lunch_eligibility = db.Column(db.Boolean, nullable=True)
    family_income_bracket_id = db.Column(db.Integer, db.ForeignKey('family_income_brackets.id'), nullable=True)
    parent_education_level_id = db.Column(db.Integer, db.ForeignKey('parent_education_levels.id'), nullable=True)
    parent_occupation_id = db.Column(db.Integer, db.ForeignKey('parent_occupations.id'), nullable=True)
    current_grade_level_id = db.Column(db.Integer, db.ForeignKey('current_grade_levels.id'), nullable=True)
    previous_schools = db.Column(db.Text, nullable=True)
    date_of_entry_school_system = db.Column(db.Date, nullable=True)
    projected_graduation_year = db.Column(db.Date, nullable=True)
    iep_status_id = db.Column(db.Integer, db.ForeignKey('iep_statuses.id'), nullable=True)
    plan_504_status = db.Column(db.Boolean, nullable=True)
    gifted_talented_program = db.Column(db.Boolean, nullable=True)
    transportation = db.Column(db.String(50), nullable=True)
    bus_route_district_id = db.Column(db.Integer, db.ForeignKey('bus_route_districts.id'), nullable=True)
    bus_route_number_id = db.Column(db.Integer, db.ForeignKey('bus_route_numbers.id'), nullable=True)
    sports_team_participation_id = db.Column(db.Integer, db.ForeignKey('sports_team_participations.id'), nullable=True)
    club_membership_id = db.Column(db.Integer, db.ForeignKey('club_memberships.id'), nullable=True)
    after_school_program = db.Column(db.Text, nullable=True)
    internet_access_id = db.Column(db.Integer, db.ForeignKey('internet_accesses.id'), nullable=True)
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
    primary_language = db.relationship('Language', foreign_keys=[primary_language_id])
    other_language = db.relationship('Language', foreign_keys=[other_language_id])
class ParentProfile(db.Model):
    __tablename__ = 'parent_profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    student_profile_id = db.Column(db.Integer, db.ForeignKey('student_profiles.id'), nullable=False)
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    user = db.relationship('User', backref=db.backref('parent_profile', uselist=False))

class TeacherProfile(db.Model):
    __tablename__ = 'teacher_profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    subject = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    user = db.relationship('User', backref=db.backref('teacher_profile', uselist=False))

class EmergencyContact(db.Model):
    __tablename__ = 'emergency_contacts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    student_profile_id = db.Column(db.Integer, db.ForeignKey('student_profiles.id'), nullable=False)
    name = db.Column(db.String(255))
    relationship = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(120))
    user = db.relationship('User', backref=db.backref('emergency_contacts', lazy=True))

class Sibling(db.Model):
    __tablename__ = 'siblings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(255))
    grade = db.Column(db.String(10))
    school = db.Column(db.String(255))
    user = db.relationship('User', backref=db.backref('siblings', lazy=True))

# Lookup tables for normalized data
class Gender(db.Model):
    __tablename__ = 'genders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class GenderIdentity(db.Model):
    __tablename__ = 'gender_identities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Pronoun(db.Model):
    __tablename__ = 'pronouns'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class FamilyStructure(db.Model):
    __tablename__ = 'family_structures'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class CustodialArrangement(db.Model):
    __tablename__ = 'custodial_arrangements'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class RacialCategory(db.Model):
    __tablename__ = 'racial_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class EthnicBackground(db.Model):
    __tablename__ = 'ethnic_backgrounds'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class PrimaryLanguage(db.Model):
    __tablename__ = 'primary_languages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class OtherLanguage(db.Model):
    __tablename__ = 'other_languages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class CitizenshipStatus(db.Model):
    __tablename__ = 'citizenship_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class ImmigrationStatus(db.Model):
    __tablename__ = 'immigration_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class FamilyIncomeBracket(db.Model):
    __tablename__ = 'family_income_brackets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class ParentEducationLevel(db.Model):
    __tablename__ = 'parent_education_levels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class ParentOccupation(db.Model):
    __tablename__ = 'parent_occupations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class CurrentGradeLevel(db.Model):
    __tablename__ = 'current_grade_levels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

class IEPStatus(db.Model):
    __tablename__ = 'iep_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class BusRouteDistrict(db.Model):
    __tablename__ = 'bus_route_districts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class BusRouteNumber(db.Model):
    __tablename__ = 'bus_route_numbers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class SportsTeamParticipation(db.Model):
    __tablename__ = 'sports_team_participations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class ClubMembership(db.Model):
    __tablename__ = 'club_memberships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class InternetAccess(db.Model):
    __tablename__ = 'internet_accesses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class DeviceOwnership(db.Model):
    __tablename__ = 'device_ownerships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class ActiveDutyParent(db.Model):
    __tablename__ = 'active_duty_parents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class VeteranStatusParent(db.Model):
    __tablename__ = 'veteran_status_parents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class HomelessStatus(db.Model):
    __tablename__ = 'homeless_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class MigrantEducationProgram(db.Model):
    __tablename__ = 'migrant_education_programs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class FosterCareInvolvement(db.Model):
    __tablename__ = 'foster_care_involvements'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class TribalAffiliation(db.Model):
    __tablename__ = 'tribal_affiliations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class ReligiousAffiliation(db.Model):
    __tablename__ = 'religious_affiliations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class ParentLifeStatus(db.Model):
    __tablename__ = 'parent_life_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class EnrollmentStatus(db.Model):
    __tablename__ = 'enrollment_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class ExitWithdrawalStatus(db.Model):
    __tablename__ = 'exit_withdrawal_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class ExitWithdrawalType(db.Model):
    __tablename__ = 'exit_withdrawal_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class NonPromotionReason(db.Model):
    __tablename__ = 'non_promotion_reasons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class DisabilityTypePrimary(db.Model):
    __tablename__ = 'disability_type_primaries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class DisabilityTypeSecondary(db.Model):
    __tablename__ = 'disability_type_secondaries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class DisabilityTypeTertiary(db.Model):
    __tablename__ = 'disability_type_tertiaries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Language(db.Model):
    __tablename__ = 'languages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

