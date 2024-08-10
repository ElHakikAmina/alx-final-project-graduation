from flask import Flask, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Connexion à la base de données SQLite
def connect_db():
    return sqlite3.connect('users.db')

# Initialiser la base de données et créer la table des utilisateurs
def init_db():
    with connect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

# Route pour l'inscription d'un utilisateur
@app.route('/register', methods=['POST'])
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

# Route pour la connexion d'un utilisateur
@app.route('/login', methods=['POST'])
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

if __name__ == '__main__':
    init_db()  # Créer la table des utilisateurs si elle n'existe pas
    app.run(debug=True)
