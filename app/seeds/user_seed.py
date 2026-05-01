from app.extensions import db
from app.models import User
from app.models import Role
from werkzeug.security import generate_password_hash

def seed_users():
    users = [
        {
            "username": "admin",
            "email": "admin@example.com",
            "password": "admin123",
            "roles": ["admin"]
        },
        {
            "username": "editor",
            "email": "editor@example.com",
            "password": "editor123",
            "roles": ["editor"]
        },

        {
            "username": "user",
            "email": "user@example.com",
            "password": "user123",
            "roles": ["user"]
        },
    ]

    for user_data in users:
        exists = User.query.filter_by(email=user_data['email']).first()

        if exists:
            continue

        new_user = User(
            username=user_data['username'],
            email=user_data['email'],
            password=generate_password_hash(user_data['password'])
        )

        db.session.add(new_user)
        db.session.flush()

        for role_name in user_data['roles']:
            role = Role.query.filter_by(name=role_name).first()

            if not role:
                print(f"Role '{role_name}' não encontrada!")
                continue

            if not role in new_user.roles:
                new_user.roles.append(role)
    
    db.session.commit()