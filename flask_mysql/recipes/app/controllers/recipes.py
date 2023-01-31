from app import app
from app.models.user import User
from app.models.recipe import Recipe
from flask import render_template, request, redirect, session
from datetime import datetime

@app.route('/recipes')
def recipes():
    if 'users_id' in session:
        # Get user by id
        user = User.get_user_by_id(session['users_id'])
        # Get recipes
        recipes = Recipe.get_all()
        return render_template('recipes.html', user = user, name = user.first_name, recipes = recipes)
    
    return redirect('/')

@app.route('/recipes/new')
def new():
    if 'users_id' in session:
        return render_template('add_recipe.html')

    return redirect('/')

@app.route('/recipes/add', methods=['POST'])
def create_recipe():
    # Validate recipe
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    # Add request form items to dictionary
    data = {k:v for k,v in request.form.items()}
    # Add users_id item to dictionary and assign it user_id value from session
    data['users_id'] = session['users_id']
    # Save data and get id
    id = Recipe.save(data)
    # Return to users page
    return redirect('/recipes')

@app.route('/recipes/<id>')
def show_recipe(id):
    # Get recipe by id
    recipe = Recipe.get_recipe_by_id(id)
    # Render recipe template with recipe data
    return render_template('recipe.html', recipe = recipe)

@app.route('/recipes/edit/<id>')
def edit(id):
    # Get recipe by id
    recipe = Recipe.get_recipe_by_id(id)
    # Check if user has access to edit this recipe
    if recipe.users_id == session['users_id']:
        recipe.date_cooked = recipe.date_cooked.strftime('%Y-%m-%d')
        print(recipe.date_cooked)
        session['recipe_id'] = recipe.id
        return render_template('/edit_recipe.html', recipe = recipe)
    
    return redirect('/recipes')

@app.route('/recipes/update', methods=['POST'])
def update_recipe():
    # Valide recipe
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipes/edit/{session["recipe_id"]}')
    # Create dictionary to hold form data
    data = {k:v for k, v in request.form.items()}
    data['id'] = session['recipe_id']
    # Update recipe
    Recipe.update(data)
    return redirect(f'/recipes')

@app.route('/recipes/delete/<id>')
def delete(id):
    Recipe.delete(id)
    return redirect('/recipes')