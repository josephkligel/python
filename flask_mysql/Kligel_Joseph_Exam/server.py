from app import app
from app.controllers import sightings, users

app.secret_key = 'This is a secret key'

if __name__ == '__main__':
    app.run(debug=True)