from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.order import Order


# Main route that shows the order records in table format
@app.route('/')
@app.route('/orders')
def index():
    # Get all orders and hand them over to the template engine
    orders = Order.get_all()
    # Return index template
    return render_template('index.html', orders = orders)

# New order page
@app.route('/order/new')
def new_order():
    title = "Log a New Order"
    action_url = "/add_order"
    # Initialize order variable with order data from form if it exists
    order = session['form'] if session.get('form') else None
    # Delete persistent form data
    session['form'] = None
    return render_template('form.html', title = title, action_url = action_url, order = order)

# Add new order
@app.route('/add_order', methods=['POST'])
def add_order():
    print(request.form)
    # Validate user information
    if not Order.validate_user(request.form):
        session['form'] = request.form
        return redirect('/order/new')
    Order.save(request.form)
    return redirect('/')

# Edit Order
@app.route('/edit/<id>')
def edit_order(id):
    # Variable initialization for page
    title = "Change Order"
    action_url = "/update_order"
    data = {'id': id}
    # Get the order by id. The id in in the url
    order = Order.get_record_by_id(data)
    # Clear out the form variable in the session
    session['form'] = None

    return render_template('form.html', title = title, action_url = action_url, order = order)

@app.route('/update_order', methods=['POST'])
def update_order():
     # Validate order information
    if not Order.validate_user(request.form):
        session['form'] = request.form
        return redirect(f'/edit/{request.form["id"]}')
    # If order information is good then save and redirect to home page
    Order.update(request.form)
    return redirect('/')