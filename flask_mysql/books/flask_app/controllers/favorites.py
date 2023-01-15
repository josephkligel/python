from flask_app import app
from flask import redirect, request, session
from flask_app.models.favorite import Favorite

@app.route('/create_favorite', methods=['POST'])
def add_favorite():
    # Create variable for return url and then delete the session's url variable
    return_url = session['url']
    session['url'] = None
    # Create data variable to hold the Favorite information
    data = {
        "author_id": request.form['author_id'],
        "book_id": request.form['book_id']
    }
    # print([f"{item}: {data[item]}" for item in data])
    Favorite.save(data)
    return redirect(f'{return_url}')