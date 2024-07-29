# app/routes.py

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.models import User, Role, StudentProfile
from app.forms import LoginForm, UserForm, UserTypeForm, UserProfileForm, BatchUpdateForm


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.users'))
    return render_template('login.html', form=form)

@main.route('/users')
@login_required
def users():
    users_query = User.query.order_by(User.id.asc())
    page = request.args.get('page', 1, type=int)
    per_page = 13
    
    search = request.args.get('search', '')
    if search:
        users_query = users_query.filter(
            (User.username.contains(search)) |
            (User.email.contains(search)) |
            (User.first_name.contains(search)) |
            (User.last_name.contains(search))
        )
    users = users_query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template('users.html', users=users.items, pagination=users, search=search)

@main.route('/user/new', methods=['GET', 'POST'])
@login_required
def new_user():
    form = UserTypeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            role_id = form.role_id.data
            print(f"Selected role_id: {role_id}")  # Debug statement
            return redirect(url_for('main.new_user_details', role_id=role_id))
        else:
            print("Form validation failed in new_user")
            print(form.errors)
    return render_template('user_type_form.html', form=form, title='Select User Type')

@main.route('/user/new/details/<int:role_id>', methods=['GET', 'POST'])
@login_required
def new_user_details(role_id):
    form = UserForm()
    print(f"Received role_id: {role_id}")  # Debug statement
    
    # Generate ID number
    current_year = datetime.now().year
    last_user = User.query.order_by(User.id.desc()).first()
    if last_user and str(last_user.id).startswith(str(current_year)):
        last_id_number = int(str(last_user.id)[4:])
        new_id_number = f"{current_year}{last_id_number + 1:04d}"
    else:
        new_id_number = f"{current_year}0001"
    
    # Generate username and email
    role_abbreviation = {
        'Student': 'stu',
        'Teacher': 'tea',
        'Parent': 'par',
        'Staff': 'sta',
        'Office': 'off'
    }
    role_name = Role.query.get(role_id).name
    print(f"Role name: {role_name}")  # Debug statement
    role_abbr = role_abbreviation.get(role_name, 'usr')
    new_username = f"{role_abbr}{new_id_number}"
    school_domain = "schooldomain.com"
    new_email = f"{new_username}@{school_domain}"
    
    if request.method == 'POST':
        form.role_id.data = role_id  # Set the role_id field explicitly
        if form.validate_on_submit():
            print("Form validated successfully in new_user_details")
            
            # Set a default password
            default_password = 'school1234'
            
            user = User(
                id=new_id_number,
                username=new_username,
                email=new_email,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                role_id=role_id,
                is_active=form.is_active.data,
                is_verified=form.is_verified.data,
                is_admin=form.is_admin.data
            )
            user.set_password(default_password)
            db.session.add(user)
            db.session.commit()
            flash('User created successfully.')
            return redirect(url_for('main.users'))
        else:
            print("Form validation failed in new_user_details")
            print(form.errors)
    
    # Pre-fill the form with generated values
    form.username.data = new_username
    form.email.data = new_email
    form.role_id.data = role_id  # Set the role_id field
    print(f"Form role_id: {form.role_id.data}")  # Debug statement
    
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
        db.session.commit()
        flash('User updated successfully.')
        return redirect(url_for('main.users'))
    form.role_id.data = user.role_id
    return render_template('user_form.html', form=form, title='Edit User')

@main.route('/user/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully.')
    return redirect(url_for('main.users'))

@main.route('/logout')
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
    form = UserProfileForm(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        flash('Profile updated successfully.')
        return redirect(url_for('main.user_profile', user_id=user.id))
    return render_template('user_profile.html', user=user, form=form)
    
@main.route('/admin/users', methods=['GET', 'POST'])
@login_required
def admin_users():
    form = UserForm()
    role_id = request.args.get('role')
    grade = request.args.get('grade')
    
    users_query = User.query
    
    if role_id:
        users_query = users_query.filter_by(role_id=role_id)
    
    if grade:
        users_query = users_query.join(StudentProfile).filter(StudentProfile.grade == grade)
    
    users = users_query.all()
    roles = Role.query.all()
    
    return render_template('admin_users.html', form=form, users=users, roles=roles)


@main.route('/admin/users/batch_update', methods=['GET', 'POST'])
@login_required
def batch_update_users():
    form = BatchUpdateForm()
    
    if request.method == 'POST':
        user_ids = request.form.getlist('user_ids')
        print("POST request received")
        print("Selected user IDs:", user_ids)
        if form.validate_on_submit():
            print("Form validated successfully")
            users = User.query.filter(User.id.in_(user_ids)).all()
            for user in users:
                if user.student_profile:
                    if form.age.data is not None:
                        user.student_profile.age = form.age.data
                    if form.grade.data:
                        user.student_profile.grade = form.grade.data
                    if form.gender_id.data is not None:
                        user.student_profile.gender_id = form.gender_id.data
                    if form.racial_category_id.data is not None:
                        user.student_profile.racial_category_id = form.racial_category_id.data
                    if form.ethnic_background_id.data is not None:
                        user.student_profile.ethnic_background_id = form.ethnic_background_id.data
                    if form.country_id.data is not None:
                        user.student_profile.country_id = form.country_id.data
                    if form.primary_language.data:
                        user.student_profile.primary_language = form.primary_language.data
                    if form.other_languages.data:
                        user.student_profile.other_languages = form.other_languages.data
                    if form.citizenship_status.data:
                        user.student_profile.citizenship_status = form.citizenship_status.data
                    if form.free_reduced_lunch_eligibility.data is not None:
                        user.student_profile.free_reduced_lunch_eligibility = form.free_reduced_lunch_eligibility.data
                    if form.projected_graduation_year.data:
                        user.student_profile.projected_graduation_year = form.projected_graduation_year.data
                    if form.iep_status.data is not None:
                        user.student_profile.iep_status = form.iep_status.data
                    if form.plan_504_status.data is not None:
                        user.student_profile.plan_504_status = form.plan_504_status.data
                    if form.gifted_talented_program.data is not None:
                        user.student_profile.gifted_talented_program = form.gifted_talented_program.data
                    if form.transportation.data:
                        user.student_profile.transportation = form.transportation.data
                    if form.bus_route_number.data:
                        user.student_profile.bus_route_number = form.bus_route_number.data
                    if form.sports_team_participation.data:
                        user.student_profile.sports_team_participation = form.sports_team_participation.data
                    if form.club_memberships.data:
                        user.student_profile.club_memberships = form.club_memberships.data
                    if form.after_school_program.data:
                        user.student_profile.after_school_program = form.after_school_program.data
                    if form.internet_access.data is not None:
                        user.student_profile.internet_access = form.internet_access.data
                    if form.device_ownership.data:
                        user.student_profile.device_ownership = form.device_ownership.data
                    if form.active_duty_military_parent.data is not None:
                        user.student_profile.active_duty_military_parent = form.active_duty_military_parent.data
                    if form.veteran_status_parent.data is not None:
                        user.student_profile.veteran_status_parent = form.veteran_status_parent.data
                    if form.homeless_status.data is not None:
                        user.student_profile.homeless_status = form.homeless_status.data
                    if form.migrant_education_program.data is not None:
                        user.student_profile.migrant_education_program = form.migrant_education_program.data
                    if form.foster_care_involvement.data is not None:
                        user.student_profile.foster_care_involvement = form.foster_care_involvement.data
                    if form.tribe_membership.data is not None:
                        user.student_profile.tribe_membership = form.tribe_membership.data
                    if form.religious_affiliation.data:
                        user.student_profile.religious_affiliation = form.religious_affiliation.data
                    if form.church_affiliation.data:
                        user.student_profile.church_affiliation = form.church_affiliation.data
            
            db.session.commit()
            flash('Batch update successful.')
            return redirect(url_for('main.admin_users'))
        else:
            print("Form validation failed")
            print(form.errors)
    else:
        user_ids = request.args.get('user_ids', '').split(',')
        print("GET request received")
        print("Selected user IDs:", user_ids)
    
    return render_template('batch_update.html', form=form, user_ids=user_ids)
