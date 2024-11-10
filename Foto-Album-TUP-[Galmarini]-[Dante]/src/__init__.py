from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask import Flask

db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()

def crear_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(obj=Config)
    
    db.init_app(app=app)
    
    from .routes import photo_bp
    
    app.register_blueprint(blueprint=photo_bp)
    
    return app

#INICIALIZA LA APLICACION