from app.extensions import db
from app.models import Role, Permission

def seed_roles():
    roles = [
        {
            "name": "admin",
            "description": "Administrador do sistema",
            "permissions": [
                "criar_livro",
                "visualizar_livro",
                "atualizar_livro",
                "deletar_livro",
                "criar_usuario",
                "visualizar_usuario",
                "atualizar_usuario",
                "deletar_usuario",
                "criar_role",
                "visualizar_role",
                "atualizar_role",
                "deletar_role",
                "criar_permission",
                "visualizar_permission",
                "atualizar_permission",
                "deletar_permission",
            ]
        },
        {
            "name": "editor",
            "description": "Editor responsável pela publicação de livros",
            "permissions": [
                "criar_livro",
                "visualizar_livro",
                "atualizar_livro",
            ]
        },
        {
            "name": "user",
            "description": "Usuário comum",
            "permissions": [
                "visualizar_livro",
            ]
        },
    ]

    for role_data in roles:
        role = Role.query.filter_by(name=role_data["name"]).first()

        if not role:
            role = Role(
                name=role_data["name"],
                description=role_data["description"]
            )
            db.session.add(role)
            db.session.flush()

        for perm_name in role_data["permissions"]:
            permission = Permission.query.filter_by(name=perm_name).first()

            if not permission:
                print(f"Permissão '{perm_name}' não encontrada!")
                continue

            if permission not in role.permissions:
                role.permissions.append(permission)

    db.session.commit()