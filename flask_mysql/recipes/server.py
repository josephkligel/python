from app import app

from app.controllers import users, recipes

app.secret_key = 'ThisIsASecretKey'

if __name__ == '__main__':
    app.run(debug=True)