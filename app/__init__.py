from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

# Crear las instancias necesarias de bcrypt, JWT y SQLAlchemy
bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Aquí puedes poner la clave segura

    # Inicializar las extensiones
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Registrar blueprints
    from .resources.user_resource import user_bp
    app.register_blueprint(user_bp)

    return app
