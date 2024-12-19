from flask import Flask, request, jsonify, abort

app = Flask(__name__)

books = []
members = []
book_id_counter = 1
member_id_counter = 1

def find_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)

def find_member(member_id):
    return next((member for member in members if member['id'] == member_id), None)

def search_books(query):
    query_lower = query.lower()
    return [book for book in books if query_lower in book['title'].lower() or query_lower in book['author'].lower()]


@app.route('/books', methods=['GET'])
def get_books():
    query = request.args.get('query')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    filtered_books = search_books(query) if query else books

    start = (page - 1) * per_page
    end = start + per_page

    return jsonify(filtered_books[start:end]), 200

@app.route('/books', methods=['POST'])
def add_book():
    global book_id_counter
    data = request.get_json()

    if not data or 'title' not in data or 'author' not in data:
        abort(400, description="Missing required fields: title, author")

    book = {
        'id': book_id_counter,
        'title': data['title'],
        'author': data['author']
    }
    books.append(book)
    book_id_counter += 1

    return jsonify(book), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = find_book(book_id)
    if not book:
        abort(404, description="Book not found")
    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = find_book(book_id)

    if not book:
        abort(404, description="Book not found")
    if not data:
        abort(400, description="Invalid data")

    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])

    return jsonify(book), 200

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = find_book(book_id)
    if not book:
        abort(404, description="Book not found")

    books.remove(book)
    return '', 204

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members), 200

@app.route('/members', methods=['POST'])
def add_member():
    global member_id_counter
    data = request.get_json()

    if not data or 'name' not in data:
        abort(400, description="Missing required field: name")

    member = {
        'id': member_id_counter,
        'name': data['name']
    }
    members.append(member)
    member_id_counter += 1

    return jsonify(member), 201

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = find_member(member_id)
    if not member:
        abort(404, description="Member not found")
    return jsonify(member), 200

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.get_json()
    member = find_member(member_id)

    if not member:
        abort(404, description="Member not found")
    if not data:
        abort(400, description="Invalid data")

    member['name'] = data.get('name', member['name'])

    return jsonify(member), 200

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = find_member(member_id)
    if not member:
        abort(404, description="Member not found")

    members.remove(member)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
