from flask import Flask

app = Flask(__name__)   # Create a new instance of the Flask class called app

@app.route('/')         # The '@' decorator associates this route with the following funciton
def hello_world():
    return 'Hello, World!'

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>')
def hello(name):
    return "Hello, " + name

@app.route('/hello/<username>/<id>')
def show_user_profile(username, id):
    return f"username: {username}, id: {id}"

if __name__ == '__main__':
    app.run(debug=True) # Run app in debug modes