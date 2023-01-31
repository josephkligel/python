from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninja_page():
    dojos = Dojo.get_all()
    return render_template('ninja.html', dojos = dojos)

@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    data = {
        # The value of dname_select is the dojo id number
        "did": request.form['dname_select'],
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "age": request.form['age'],
    }

    print(data)
    Ninja.save(data)

    return redirect(f'/show/dojo/{data["did"]}')

@app.route('/edit/ninjas/<id>')
def edit_ninja(id):
    data = {"id": id}
    dojos = Dojo.get_all()
    ninja = Ninja.get_ninja_by_id(data)
    url = session['dojo_url']
    print(ninja)
    return render_template('edit.html', dojos = dojos, ninja = ninja, url = url)

@app.route('/update_ninja', methods=['POST'])
def update_ninja():
    data = {
        "id": request.form['id'],
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "age": request.form['age'],
        # Dname select name provides the dojo id needed to update a ninja's record
        "dojo_id": request.form['dname_select']
    }
    # Updating record
    Ninja.update(data)
    print(data)

    return redirect(f'/show/dojo/{data["dojo_id"]}')

@app.route('/delete/ninjas/<id>')
def delete_ninja(id):
    data = {'id': id}
    print(Ninja.delete(data))
    
    return redirect(session['dojo_url'])