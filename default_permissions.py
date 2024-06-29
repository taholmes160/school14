# default_permissions.py

default_permissions = {
    "Principal": ["read_grades", "read_users", "manage_users"],
    "Teacher": ["create_grades", "read_grades", "update_grades", "delete_grades", "read_users"],
    "Student": ["read_grades"],
    "Parent": ["read_grades"],
    # Add other roles and their default permissions here
}

def populate_permissions():
    from app import create_app, db
    from app.models import Role, Permission, RolePermission

    app = create_app()
    with app.app_context():
        for role_name, permissions in default_permissions.items():
            role = Role.query.filter_by(name=role_name).first()
            if not role:
                role = Role(name=role_name)
                db.session.add(role)
                db.session.commit()

            for permission_name in permissions:
                permission = Permission.query.filter_by(name=permission_name).first()
                if not permission:
                    permission = Permission(name=permission_name)
                    db.session.add(permission)
                    db.session.commit()

                role_permission = RolePermission.query.filter_by(role_id=role.id, permission_id=permission.id).first()
                if not role_permission:
                    role_permission = RolePermission(role_id=role.id, permission_id=permission.id)
                    db.session.add(role_permission)
                    db.session.commit()

        print("Default permissions have been populated.")

if __name__ == "__main__":
    populate_permissions()
