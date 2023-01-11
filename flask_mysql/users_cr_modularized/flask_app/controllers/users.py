from flask_app import app

from flask import render_template, request, redirect

from flask_app.models.user import User

@app.route('/users')
def users():
    users = User.get_all()
    print(users)
    return render_template('users.html', all_users = users)

@app.route('/users/new')
def new_user():
    return render_template('create.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    id = User.save(data)

    return redirect(f'/show/{id}')

@app.route('/show/<id>')
def show_user(id):
    data = {
        "id": id
    }
    record = User.get_record_by_id(data)[0]
    print(record)

    return render_template('show.html', record=record)

@app.route('/user/edit/<id>')
def edit_user(id):
    data = {"id": id}
    record = User.get_record_by_id(data)[0]
    
    return render_template('edit.html', record=record)

@app.route('/update_user', methods=['POST'])
def update_user():
    print(request.form)
    User.update_record(request.form)

    return redirect(f'/show/{request.form["id"]}')

@app.route('/delete/<id>')
def delete_user(id):
    data = {'id': id}
    print(id)
    User.delete_record(data)

    return redirect('/users')