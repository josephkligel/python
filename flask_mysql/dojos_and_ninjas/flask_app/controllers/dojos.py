from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# Renders form for adding new dojos and shows all dojos in dojos table
@app.route('/')
@app.route('/dojos')
def show_dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)

# Creates and adds new dojo to dojos table
@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        'dname': request.form['dname']
    }
    Dojo.save(data)
    return redirect('/dojos')

# Show individual dojo pages
@app.route('/show/dojo/<id>')
def show_dojo(id):
    # Retreive dojo from dojos table
    data = {"id": id}
    dojo = Dojo.get_dojo_by_id(data)[0]
    # Get all ninjas from database by location
    ninjas = Ninja.get_ninjas_by_dojo_id(data)
    session['dojo_url'] = request.url
    return render_template('dojo_record.html', dojo = dojo, ninjas = ninjas)