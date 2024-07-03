from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Role, StudentProfile, ParentProfile, TeacherProfile, EmergencyContact, Sibling
from app.forms import LoginForm, UserForm, StudentProfileForm, ParentProfileForm, TeacherProfileForm
from flask_paginate import Pagination, get_page_parameter

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    search = request.args.get('search')
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    if search:
        users_query = User.query.filter(User.last_name.contains(search))
    else:
        users_query = User.query
    users = users_query.paginate(page=page, per_page=per_page, error_out=False)
    pagination = Pagination(page=page, total=users.total, search=search, record_name='users')
    return render_template('users.html', users=users.items, pagination=pagination, search=search)

@main.route('/user/new', methods=['GET', 'POST'])
@login_required
def new_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            role_id=form.role_id.data,
            is_active=form.is_active.data,
            is_verified=form.is_verified.data,
            is_admin=form.is_admin.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User created successfully.')
        return redirect(url_for('main.users'))
    return render_template('user_form.html', form=form, title='New User')

@main.route('/user/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.role_id = form.role_id.data
        user.is_active = form.is_active.data
        user.is_verified = form.is_verified.data
        user.is_admin = form.is_admin.data
        if form.password.data:
            user.set_password(form.password.data)
        db.session.commit()
        flash('User updated successfully.')
        return redirect(url_for('main.users'))
    return render_template('user_form.html', form=form, title='Edit User')

@main.route('/user/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully.')
    return redirect(url_for('main.users'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.users'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route('/status')
def status():
    return f"Authenticated: {current_user.is_authenticated}, User: {current_user}"

@main.route('/user/<int:user_id>/profile', methods=['GET', 'POST'])
@login_required
def user_profile(user_id):
    user = User.query.get_or_404(user_id)
    if user.role.name == 'Student':
        form = StudentProfileForm(obj=user.student_profile)
    elif user.role.name == 'Parent':
        form = ParentProfileForm(obj=user.parent_profile)
    elif user.role.name == 'Teacher':
        form = TeacherProfileForm(obj=user.teacher_profile)
    else:
        form = None

    if form and form.validate_on_submit():
        if user.role.name == 'Student':
            if not user.student_profile:
                user.student_profile = StudentProfile(user_id=user.id)
            user.student_profile.age = form.age.data
            user.student_profile.grade = form.grade.data
            user.student_profile.address = form.address.data
            user.student_profile.parent_guardian = form.parent_guardian.data
            user.student_profile.demographic_info = form.demographic_info.data
            user.student_profile.discipline_records = form.discipline_records.data
            user.student_profile.gender_id = form.gender_id.data
            user.student_profile.racial_category_id = form.racial_category_id.data
            user.student_profile.ethnic_background_id = form.ethnic_background_id.data
            user.student_profile.country_id = form.country_id.data
            user.student_profile.date_of_birth = form.date_of_birth.data
            user.student_profile.place_of_birth = form.place_of_birth.data
            user.student_profile.pronouns = form.pronouns.data
            user.student_profile.phone_number = form.phone_number.data
            user.student_profile.email = form.email.data
            user.student_profile.family_structure = form.family_structure.data
            user.student_profile.custodial_arrangements = form.custodial_arrangements.data
            user.student_profile.hispanic_latino_origin = form.hispanic_latino_origin.data
            user.student_profile.primary_language = form.primary_language.data
            user.student_profile.other_languages = form.other_languages.data
            user.student_profile.english_proficiency = form.english_proficiency.data
            user.student_profile.esl_ell_status = form.esl_ell_status.data
            user.student_profile.citizenship_status = form.citizenship_status.data
            user.student_profile.immigration_status = form.immigration_status.data
            user.student_profile.date_of_entry_us = form.date_of_entry_us.data
            user.student_profile.free_reduced_lunch_eligibility = form.free_reduced_lunch_eligibility.data
            user.student_profile.family_income_bracket = form.family_income_bracket.data
            user.student_profile.parent_education_level = form.parent_education_level.data
            user.student_profile.parent_occupation = form.parent_occupation.data
            user.student_profile.current_grade_level = form.current_grade_level.data
            user.student_profile.previous_schools = form.previous_schools.data
            user.student_profile.date_of_entry_school_system = form.date_of_entry_school_system.data
            user.student_profile.projected_graduation_year = form.projected_graduation_year.data
            user.student_profile.iep_status = form.iep_status.data
            user.student_profile.plan_504_status = form.plan_504_status.data
            user.student_profile.gifted_talented_program = form.gifted_talented_program.data
            user.student_profile.transportation = form.transportation.data
            user.student_profile.bus_route_number = form.bus_route_number.data
            user.student_profile.sports_team_participation = form.sports_team_participation.data
            user.student_profile.club_memberships = form.club_memberships.data
            user.student_profile.after_school_program = form.after_school_program.data
            user.student_profile.internet_access = form.internet_access.data
            user.student_profile.device_ownership = form.device_ownership.data
            user.student_profile.active_duty_military_parent = form.active_duty_military_parent.data
            user.student_profile.veteran_status_parent = form.veteran_status_parent.data
            user.student_profile.homeless_status = form.homeless_status.data
            user.student_profile.migrant_education_program = form.migrant_education_program.data
            user.student_profile.foster_care_involvement = form.foster_care_involvement.data
            user.student_profile.tribe_membership = form.tribe_membership.data
            user.student_profile.religious_affiliation = form.religious_affiliation.data
            user.student_profile.church_affiliation = form.church_affiliation.data
            user.student_profile.school_assigned_id = form.school_assigned_id.data
            user.student_profile.state_assigned_id = form.state_assigned_id.data
            user.student_profile.national_id = form.national_id.data
        elif user.role.name == 'Parent':
            if not user.parent_profile:
                user.parent_profile = ParentProfile(user_id=user.id)
            user.parent_profile.address = form.address.data
            user.parent_profile.phone_number = form.phone_number.data
        elif user.role.name == 'Teacher':
            if not user.teacher_profile:
                user.teacher_profile = TeacherProfile(user_id=user.id)
            user.teacher_profile.subject = form.subject.data
            user.teacher_profile.address = form.address.data
            user.teacher_profile.phone_number = form.phone_number.data
        db.session.commit()
        flash('Profile updated successfully.')
        return redirect(url_for('main.user_profile', user_id=user.id))

    return render_template('user_profile.html', form=form, user=user)
