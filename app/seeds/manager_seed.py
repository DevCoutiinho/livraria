from .permission_seed import seed_permissions
from .role_seed import seed_roles
from .user_seed import seed_users

def run_all_seeds():
    seed_permissions()
    seed_roles()
    seed_users()