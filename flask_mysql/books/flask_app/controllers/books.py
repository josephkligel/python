from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.models.favorite import Favorite

@app.route('/books')
def show_books():
    books = Book.get_all()
    print(books)
    return render_template('books.html', books = books)

@app.route('/create_book', methods=['POST'])
def add_book():
    Book.save(request.form)
    return redirect('/books')

@app.route('/books/<id>')
def show_book(id):
    # Define data dictionary containing book's id
    data = {"id": id}
    # Save url
    session['url'] = request.url
    # Get book record by its id
    book = Book.get_records_by_id(data)[0]
    # Define book title to be displayed by template header
    title = book.title
    # Get favorites by book id
    favorites_by_book_id = Favorite.get_records_by_type("book_id", data)
    # Create and append list of authors who favorited book
    authors_who_favorited = []
    for favorite in favorites_by_book_id:
        author = Author.get_records_by_id(dict(id = favorite.author_id))[0]
        authors_who_favorited.append(author)
    # Make a list of the authors who have not favorited
    # Get all authors first and create an empty list
    authors = Author.get_all()
    non_fave_authors = []
    for aut in authors:
        if aut.name not in [a.name for a in authors_who_favorited]:
            non_fave_authors.append(aut)
    
    return render_template('show_book.html', book_id = data['id'], title = title, authors = authors_who_favorited, non_fave_authors = non_fave_authors)