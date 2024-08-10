from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

bp = Blueprint('auth', __name__, url_prefix='/auth')

def connect_db():
    return sqlite3.connect('users.db')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Nom d'utilisateur et mot de passe sont requis."}), 400

    hashed_password = generate_password_hash(password, method='sha256')

    try:
        with connect_db() as conn:
            conn.execute('''
                INSERT INTO users (username, password) VALUES (?, ?)
            ''', (username, hashed_password))
            conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"message": "Le nom d'utilisateur existe déjà."}), 409

    return jsonify({"message": "Inscription réussie!"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Nom d'utilisateur et mot de passe sont requis."}), 400

    with connect_db() as conn:
        user = conn.execute('''
            SELECT * FROM users WHERE username = ?
        ''', (username,)).fetchone()

    if user and check_password_hash(user[2], password):
        return jsonify({"message": "Connexion réussie!"}), 200
    else:
        return jsonify({"message": "Nom d'utilisateur ou mot de passe incorrect."}), 401
