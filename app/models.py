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
    
    def has_permission(self, permission):
        if self.role and self.role.permissions:
            return permission in self.role.permissions.split(',')
        return False

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
    age = db.Column(db.Integer)
    grade = db.Column(db.String(10))
    address = db.Column(db.String(255))
    parent_guardian = db.Column(db.String(255))
    demographic_info = db.Column(db.Text)
    discipline_records = db.Column(db.Text)
    gender_id = db.Column(db.Integer, db.ForeignKey('genders.id'))
    racial_category_id = db.Column(db.Integer, db.ForeignKey('racial_categories.id'))
    ethnic_background_id = db.Column(db.Integer, db.ForeignKey('ethnic_backgrounds.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    date_of_birth = db.Column(db.Date)
    place_of_birth = db.Column(db.String(255))
    pronouns = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(120))
    family_structure = db.Column(db.String(50))
    custodial_arrangements = db.Column(db.Text)
    hispanic_latino_origin = db.Column(db.Boolean)
    primary_language = db.Column(db.String(50))
    other_languages = db.Column(db.String(50))
    english_proficiency = db.Column(db.String(50))
    esl_ell_status = db.Column(db.Boolean)
    citizenship_status = db.Column(db.String(50))
    immigration_status = db.Column(db.String(50))
    date_of_entry_us = db.Column(db.Date)
    free_reduced_lunch_eligibility = db.Column(db.Boolean)
    family_income_bracket = db.Column(db.String(50))
    parent_education_level = db.Column(db.String(50))
    parent_occupation = db.Column(db.String(50))
    current_grade_level = db.Column(db.String(10))
    previous_schools = db.Column(db.Text)
    date_of_entry_school_system = db.Column(db.Date)
    projected_graduation_year = db.Column(db.Date)
    iep_status = db.Column(db.Boolean)
    plan_504_status = db.Column(db.Boolean)
    gifted_talented_program = db.Column(db.Boolean)
    transportation = db.Column(db.String(50))
    bus_route_number = db.Column(db.String(50))
    sports_team_participation = db.Column(db.Text)
    club_memberships = db.Column(db.Text)
    after_school_program = db.Column(db.Text)
    internet_access = db.Column(db.Boolean)
    device_ownership = db.Column(db.String(50))
    active_duty_military_parent = db.Column(db.Boolean)
    veteran_status_parent = db.Column(db.Boolean)
    homeless_status = db.Column(db.Boolean)
    migrant_education_program = db.Column(db.Boolean)
    foster_care_involvement = db.Column(db.Boolean)
    tribe_membership = db.Column(db.Boolean)
    religious_affiliation = db.Column(db.String(50))
    church_affiliation = db.Column(db.String(50))
    school_assigned_id = db.Column(db.String(50))
    state_assigned_id = db.Column(db.String(50))
    national_id = db.Column(db.String(50))
    user = db.relationship('User', backref=db.backref('student_profile', uselist=False))

class ParentProfile(db.Model):
    __tablename__ = 'parent_profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
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

class RacialCategory(db.Model):
    __tablename__ = 'racial_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class EthnicBackground(db.Model):
    __tablename__ = 'ethnic_backgrounds'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
