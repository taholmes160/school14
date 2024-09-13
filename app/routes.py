from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, Blueprint, send_file
from flask_login import current_user, login_user, logout_user, login_required
from weasyprint import HTML
from io import BytesIO
from app import db
from app.models import User, Role, StudentProfile, EthnicBackground, Language
from app.forms import LoginForm, UserForm, UserTypeForm, UserProfileForm, BatchUpdateForm, AdvancedSearchForm, SelectGradeForm

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
    users_query = User.query.outerjoin(StudentProfile)
    
    advanced_search_form = AdvancedSearchForm()
    if advanced_search_form.validate_on_submit() or request.args.get('filter_field'):
        filter_field = request.args.get('filter_field', advanced_search_form.filter_field.data)
        filter_value = request.args.get('filter_value', advanced_search_form.filter_value.data)
        
        print(f"Filter Field: {filter_field}")  # Debug statement
        print(f"Filter Value: {filter_value}")  # Debug statement
        
        if filter_field == 'grade':
            users_query = users_query.filter(StudentProfile.grade == filter_value)
        elif filter_field == 'ethnic_origin':
            users_query = users_query.filter(StudentProfile.ethnic_background_id == filter_value)
    
    sort_by = request.args.get('sort_by', default='id', type=str)
    sort_order = request.args.get('sort_order', default='asc', type=str)
    
    if sort_by == 'grade':
        users_query = users_query.order_by(StudentProfile.grade.asc() if sort_order == 'asc' else StudentProfile.grade.desc())
    elif sort_by == 'age':
        users_query = users_query.order_by(StudentProfile.age.asc() if sort_order == 'asc' else StudentProfile.age.desc())
    else:
        users_query = users_query.order_by(getattr(User, sort_by).asc() if sort_order == 'asc' else getattr(User, sort_by).desc())
    
    users = users_query.all()
    
    form = BatchUpdateForm()  # Create an instance of the form
    
    return render_template('users.html', users=users, form=form, advanced_search_form=advanced_search_form, sort_by=sort_by, sort_order=sort_order)

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
    form.role_id.data = role_id  # Set the role_id in the form

    # Determine the user type prefix based on the role_id
    role = Role.query.get(role_id)
    if role.name.lower() == 'student':
        user_type_prefix = 'stu'
    elif role.name.lower() == 'teacher':
        user_type_prefix = 'tea'
    elif role.name.lower() == 'staff':
        user_type_prefix = 'sta'
    elif role.name.lower() == 'parent':
        user_type_prefix = 'par'
    else:
        user_type_prefix = 'usr'  # Default prefix

    form.user_type_prefix.data = user_type_prefix  # Set the user type prefix in the form

    # Generate ID number
    current_year = datetime.now().year
    last_user = User.query.order_by(User.id.desc()).first()
    if last_user:
        last_id = last_user.id
        new_id = last_id + 1
    else:
        new_id = int(f"{current_year}0001")

    # Generate username and email
    username = f"{user_type_prefix}{new_id}"
    email = f"{new_id}@school.edu"

    # Set the default password
    password = 'school1234'

    # Pre-fill the form fields
    form.username.data = username
    form.email.data = email
    form.password.data = password
    form.confirm_password.data = password

    if form.validate_on_submit():
        # Create the new user
        new_user = User(
            id=new_id,
            username=form.username.data,
            email=form.email.data,
            role_id=role_id,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            is_active=form.is_active.data,
            is_verified=form.is_verified.data,
            is_admin=form.is_admin.data
        )
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('New user created successfully')
        return redirect(url_for('main.users'))

    return render_template('user_form.html', form=form, title='New User Details')

@main.route('/user/profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def user_profile(user_id):
    user = User.query.get_or_404(user_id)
    
    # Ensure the student profile exists
    if user.student_profile is None:
        user.student_profile = StudentProfile(user_id=user.id)
        db.session.add(user.student_profile)
        db.session.commit()

    form = UserProfileForm(obj=user.student_profile)  # Populate the form with student profile data

    if form.validate_on_submit():
        form.populate_obj(user.student_profile)
        db.session.commit()
        flash('Profile updated successfully')
        return redirect(url_for('main.users'))  # Redirect to the users list

    return render_template('user_profile.html', user=user, form=form)

@main.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(obj=user)  # Populate the form with user data

    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        flash('User updated successfully')
        return redirect(url_for('main.users'))

    return render_template('user_form.html', form=form, title='Edit User')

@main.route('/user/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully')
    return redirect(url_for('main.users'))

@main.route('/report/grade', methods=['GET', 'POST'])
@login_required
def report_grade():
    form = SelectGradeForm()
    if form.validate_on_submit():
        grade = form.grade.data
        students = User.query.join(StudentProfile).filter(StudentProfile.grade == grade).all()
        
        # Render the HTML template for the PDF
        html = render_template('report_grade.html', students=students, grade=grade)
        
        # Generate the PDF
        pdf = HTML(string=html).write_pdf()
        
        # Create a response with the PDF file
        response = BytesIO()
        response.write(pdf)
        response.seek(0)
        
        return send_file(response, mimetype='application/pdf', as_attachment=True, download_name=f'grade_{grade}_report.pdf')
    
    return render_template('select_grade.html', form=form)
