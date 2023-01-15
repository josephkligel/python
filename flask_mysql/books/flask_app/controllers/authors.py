from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.author import Author
from flask_app.models.favorite import Favorite
from flask_app.models.book import Book

@app.route('/')
@app.route('/authors')
def show_authors():
    authors = Author.get_all()
    return render_template('/authors.html', authors = authors)

@app.route('/create_author', methods=['POST'])
def add_author():
    Author.save(request.form)
    return redirect('/authors')

@app.route('/authors/<id>')
def show_author(id):
    # Define a dictionary with the author's id passed into the url parameter
    data = {'id': id}
    # Save current author's url
    session['url'] = request.url
    # Get the author by id. Method returns list but only one record in the list, the first one
    author = Author.get_records_by_id(data)[0]
    title = f"{author.name}'s Favorite Books"
    # Retreive and list favorite books by author's id
    favorites_by_author = Favorite.get_records_by_type("author_id", data)
    authors_fav_books = []
    for fave in favorites_by_author:
        book = Book.get_records_by_id(dict(id = fave.book_id))[0]
        authors_fav_books.append(book)
    # Retreive and list any book that is not currently the author's favorite
    books = Book.get_all()
    non_fave_books = []
    for book in books:
        if book.id not in [b.id for b in authors_fav_books]:
            non_fave_books.append(book)
    
    return render_template('show_author.html', title = title, id = data['id'], books = authors_fav_books, non_fave_books = non_fave_books)