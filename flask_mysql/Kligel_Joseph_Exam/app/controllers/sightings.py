from app import app
from app.models import sighting, user
from flask import render_template, redirect, request, session

# Table of Contents
# Dashboard route
# New sighting route
# Add sighting route
# Delete sighting route
# Edit sighting route
# Update sighting route
# Show sighting

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    # Create variables for logged in user and sightings
    logged_in_user = user.User.get_by_id(session['user_id'])
    sightings = sighting.Sighting.get_all()

    return render_template('dashboard.html', user = logged_in_user, sightings = sightings)

@app.route('/new/sighting')
def new():
    logged_in_user = user.User.get_by_id(session['user_id'])
    return render_template('new.html', user = logged_in_user)

@app.route('/add/sighting', methods=['POST'])
def add_sighting():
    # Validate sighting
    if not sighting.Sighting.validate_sighting(request.form):
        return redirect('/new/sighting')
    # Add request form fields to dictionary
    data = {k:v for k,v in request.form.items()}
    # Add users_id item to dictionary and assign it user_id value from session
    data['users_id'] = session['user_id']
    # Save sighting data
    sighting.Sighting.save(data)
    # Return to users page
    return redirect('/dashboard')

@app.route('/delete/<id>')
def delete(id):
    # Delete sighting by id
    sighting.Sighting.delete(id)

    return redirect('/dashboard')

@app.route('/edit/<id>')
def edit(id):
    # Get logged in user
    logged_in_user = user.User.get_by_id(session['user_id'])
    # Get sighting record
    sighting_record = sighting.Sighting.get_by_id(id)
    # Format date
    sighting_record.date_of_sighting = sighting_record.date_of_sighting.strftime('%Y-%m-%d')
    # Save sighting record in session
    session['sighting_id'] = sighting_record.id
    return render_template('edit.html', user = logged_in_user, sighting = sighting_record)

@app.route('/update', methods=['POST'])
def update():
    # Valide sighting
    if not sighting.Sighting.validate_sighting(request.form):
        return redirect(f'/edit/{session["sighting_id"]}')
    # Create dictionary to hold form data
    data = {k:v for k, v in request.form.items()}
    data['id'] = session['sighting_id']
    # Update recipe
    sighting.Sighting.update(data)

    return redirect(f'/dashboard')

@app.route('/show/<id>')
def show(id):
    # Get user by id
    user_record = user.User.get_by_id(session['user_id'])
    # Get sighting by id
    sighting_record = sighting.Sighting.get_by_id(id)
    print(sighting_record.user.first_name)
    return render_template('sighting.html', user = user_record, sighting = sighting_record)