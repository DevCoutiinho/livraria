from app.extensions import db
from app.models import Permission

def seed_permissions():
    permissions = [
        {
            "name": "criar_livro"
        },
        {
            "name": "visualizar_livro"
        },
        {
            "name": "atualizar_livro"
        },
        {
            "name": "deletar_livro"
        },
        {
            "name": "criar_usuario"
        },
        {
            "name": "visualizar_usuario"
        },
        {
            "name": "atualizar_usuario"
        },
        {
            "name": "deletar_usuario"
        },
        {
            "name": "criar_role"
        },
        {
            "name": "visualizar_role"
        },
        {
            "name": "atualizar_role"
        },
        {
            "name": "deletar_role"
        },
        {
            "name": "criar_permission"
        },
        {
            "name": "visualizar_permission",
        },
        {
            "name": "atualizar_permission"
        },
        {
            "name": "deletar_permission"
        },
    ]
    
    for permission in permissions:
        exists = Permission.query.filter_by(name=permission["name"]).first()

        if not exists:
            new_permission = Permission(name=permission['name'])
            db.session.add(new_permission)
    
    db.session.commit()