# app/routes.py

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.models import User, Role, StudentProfile, EthnicBackground
from app.forms import LoginForm, UserForm, UserTypeForm, UserProfileForm, BatchUpdateForm, AdvancedSearchForm

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

@main.route('/users', methods=['GET', 'POST'])
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
    
    advanced_search_form = AdvancedSearchForm()
    if advanced_search_form.validate_on_submit():
        if advanced_search_form.grade.data:
            users_query = users_query.filter(User.student_profile.has(grade=advanced_search_form.grade.data))
        if advanced_search_form.ethnic_origin.data and advanced_search_form.ethnic_origin.data != 0:
            users_query = users_query.filter(User.student_profile.has(ethnic_background_id=advanced_search_form.ethnic_origin.data))
        if advanced_search_form.search_empty_fields.data:
            users_query = users_query.filter(
                (User.first_name == None) | (User.first_name == '') |
                (User.last_name == None) | (User.last_name == '') |
                (User.email == None) | (User.email == '') |
                (User.username == None) | (User.username == '')
            )
    
    users = users_query.paginate(page=page, per_page=per_page, error_out=False)
    
    form = BatchUpdateForm()  # Create an instance of the form
    
    return render_template('users.html', users=users.items, pagination=users, search=search, form=form, advanced_search_form=advanced_search_form)


@main.route('/user/new', methods=['GET', 'POST'])
@login_required
def new_user():
    form = UserTypeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            role_id = form.role_id.data
            print(f"Selected role_id: {role_id}")  # Debug statement
            return redirect(url_for('main.new_user_details', role_id=role_id))
    return render_template('user_type_form.html', form=form, title='New User')

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
            
            # Create student profile if the user is a student
            if user.role.name == 'Student':
                student_profile = StudentProfile(user_id=user.id)
                db.session.add(student_profile)
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

@main.route('/batch_update', methods=['POST'])
@login_required
def batch_update():
    form = BatchUpdateForm()
    if form.validate_on_submit():
        user_ids = request.form.getlist('user_ids')
        if not user_ids:
            flash('No users selected for update.')
            return redirect(url_for('main.users'))
        
        for user_id in user_ids:
            user = User.query.get(user_id)
            if user and user.role.name == 'Student':
                if not user.student_profile:
                    user.student_profile = StudentProfile(user_id=user.id)
                if form.set_age.data is not None:
                    user.student_profile.age = form.set_age.data
                if form.set_grade.data:
                    user.student_profile.grade = form.set_grade.data
        db.session.commit()
        flash('Batch update successful.')
        return redirect(url_for('main.users'))
    return render_template('batch_update.html', form=form)