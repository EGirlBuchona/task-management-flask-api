from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ..models.task import User, db

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Verificar si el nombre de usuario ya existe
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Username already exists"}), 400

    # Crear nuevo usuario
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])

    # Guardar el usuario en la base de datos
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Verificar si el usuario existe y la contraseña es correcta
    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({"message": "Invalid credentials"}), 401

    # Generar token JWT
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200
