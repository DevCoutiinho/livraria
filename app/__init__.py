from flask import Flask
from .extensions import db, migrate
from .commands import seed_command
from app.routes.auth.auth_routes import auth_bp
from app.routes.auth.auth_pages import auth_pages_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.DevelopmentConfig')

    db.init_app(app)
    migrate.init_app(app, db)
    
    from . import models
    app.cli.add_command(seed_command)

    app.register_blueprint(auth_bp)
    app.register_blueprint(auth_pages_bp)
    
    return app