from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'This is a secret, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def get_form_info():
    print(request.form)
    session['results'] = request.form
    return redirect('/results')

@app.route('/results')
def show_results():
    return render_template('results.html', results=session['results'])

if __name__ == '__main__':
    app.run(debug=True)