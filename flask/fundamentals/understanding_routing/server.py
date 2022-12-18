from flask import Flask

app = Flask(__name__)

# Hello World!
@app.route('/')
def hello_world():
    return 'Hello World!'

# Hello Dojo
@app.route('/dojo')
def hello_dojo():
    return 'Hello Dojo'

# Say hi to variable names
@app.route('/say/<name>')
def hello(name):
    name = str(name)
    return f'Hi {name}!'

# Repeat a word a number of times
@app.route('/repeat/<num>/<name>')
def hello_iterate(num, name):
    num_int = int(num)
    name = str(name)

    yield num + '</br>'

    for i in range(num_int):
        yield name + '</br>'

# Return error
@app.errorhandler(404)
def error(e):
    return 'Sorry! No response. Try again.'

if __name__ == '__main__':
    app.run(debug=True)