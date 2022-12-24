from flask import Flask, render_template, session, redirect, request
import base64

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

# ------------ Main route ---------- 
# Adds 1 to the visited_count everytime the route is loaded
@app.route('/')
def index():
    if 'visited_count' in session:
        print('keys exists!')
    else:
        session['visited_count'] = 0
        session['count'] = 0
    
    session['visited_count'] += 1

    return render_template('index.html', visited_count=session['visited_count'], count=session['count'])

# ------------- Destroy session cookie route ---------------
# Delete session cookie and start counts over
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

# -------------- Customizing Counts ------------------
# ------------ Add 2 to count when "+2" button is pressed
@app.route('/plus2')
def plus_two():
    if 'count' in session:
        print('key exists!')
    else:
        session['count'] = 0

    session['count'] += 2

    return redirect('/')

# Reset count when "reset" button is pressed
@app.route('/reset')
def reset_count():
    session['count'] = 0

    return redirect('/')

# Use a form to determine the custom number to add to the count
@app.route('/custom-count', methods=['POST'])
def custom_count():
    if 'count' in session:
        print('key exists!')
    else:
        session['count'] = 0

    addition = int(request.form['custom-count'])

    session['count'] += addition

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

    result = base64.urlsafe_b64decode('eyJjb3VudCI6MiwidmlzaXRlZF9jb3VudCI6Mn0.Y6d2FA.ycynv0DsnoL-YvyXvFvsppv71-E')
    print(result)