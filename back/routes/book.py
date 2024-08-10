from flask import Blueprint, request, jsonify
import sqlite3

bp = Blueprint('book', __name__, url_prefix='/books')

def connect_db():
    return sqlite3.connect('books.db')

@bp.route('/add', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    isbn = data.get('isbn')

    if not title or not author or not isbn:
        return jsonify({"message": "Tous les champs sont requis."}), 400

    try:
        with connect_db() as conn:
            conn.execute('''
                INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)
            ''', (title, author, isbn))
            conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"message": "Le livre avec cet ISBN existe déjà."}), 409

    return jsonify({"message": "Livre ajouté avec succès!"}), 201

@bp.route('/delete/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    with connect_db() as conn:
        cur = conn.cursor()
        cur.execute('''
            DELETE FROM books WHERE id = ?
        ''', (book_id,))
        if cur.rowcount == 0:
            return jsonify({"message": "Livre non trouvé."}), 404
        conn.commit()

    return jsonify({"message": "Livre supprimé avec succès!"}), 200

@bp.route('/modify/<int:book_id>', methods=['PUT'])
def modify_book(book_id):
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    isbn = data.get('isbn')

    with connect_db() as conn:
        cur = conn.cursor()
        if title:
            cur.execute('''
                UPDATE books SET title = ? WHERE id = ?
            ''', (title, book_id))
        if author:
            cur.execute('''
                UPDATE books SET author = ? WHERE id = ?
            ''', (author, book_id))
        if isbn:
            cur.execute('''
                UPDATE books SET isbn = ? WHERE id = ?
            ''', (isbn, book_id))
        if cur.rowcount == 0:
            return jsonify({"message": "Livre non trouvé."}), 404
        conn.commit()

    return jsonify({"message": "Livre modifié avec succès!"}), 200

@bp.route('/search', methods=['GET'])
def search_book():
    title = request.args.get('title')

    if not title:
        return jsonify({"message": "Le titre du livre est requis."}), 400

    with connect_db() as conn:
        books = conn.execute('''
            SELECT * FROM books WHERE title LIKE ?
        ''', (f'%{title}%',)).fetchall()

    if not books:
        return jsonify({"message": "Aucun livre trouvé."}), 404

    results = [{"id": book[0], "title": book[1], "author": book[2], "isbn": book[3]} for book in books]
    return jsonify(results), 200
