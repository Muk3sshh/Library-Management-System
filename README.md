# Library-Management-System
This project is a Flask-based API for managing a library system. It supports CRUD operations for books and members, with additional functionality for searching books by title or author and paginated responses.

How to Run the Project

Prerequisites

Python 3.7 or higher

Flask library (comes pre-installed with Python)

Steps

Clone the repository:

git clone <repository-link>
cd <repository-folder>

Run the application:

python app.py

The API will be available at http://127.0.0.1:5000/.

Use tools like curl, Postman, or a browser to interact with the endpoints.

API Endpoints

Books

GET /books: Fetch all books with optional search (query), pagination (page and per_page).

POST /books: Add a new book (requires title and author).

GET /books/<book_id>: Fetch details of a specific book.

PUT /books/<book_id>: Update details of a specific book.

DELETE /books/<book_id>: Remove a book from the system.

Members

GET /members: Fetch all members.

POST /members: Add a new member (requires name).

GET /members/<member_id>: Fetch details of a specific member.

PUT /members/<member_id>: Update details of a specific member.

DELETE /members/<member_id>: Remove a member from the system.

Design Choices

In-memory Data Storage:
The data is stored in Python lists (books and members) for simplicity. This avoids the need for a database but limits scalability.

Utility Functions:
Helper functions (find_book, find_member, search_books) streamline common operations, enhancing readability and maintainability.

Validation and Error Handling:
The API validates inputs and returns appropriate HTTP status codes (e.g., 400 for bad requests, 404 for not found).

Pagination and Search:
Built-in support for paginated responses and searching ensures usability with large datasets.

Assumptions and Limitations

In-memory Storage:

Data will be lost when the application restarts.

Not suitable for production environments.

No Authentication:

The API does not include user authentication or token-based security.

Simplified Data Model:

Books have only title and author fields.

Members have only a name field.

No Concurrency Support:

The application does not handle concurrent requests modifying shared resources.

Error Responses:

Errors return a description field in the response for debugging purposes, which might expose internal details.

This application serves as a foundational structure for a library management system. With additional features like database integration and authentication, it can be expanded for real-world use.

