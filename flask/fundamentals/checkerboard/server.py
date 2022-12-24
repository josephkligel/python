from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<rows>')
@app.route('/<rows>/<cols>')
@app.route('/<rows>/<cols>/<color1>/<color2>')
def index(cols=8, rows=8, color1='red', color2='black'):
    cols = int(cols)
    rows = int(rows)
    return render_template('index.html', cols=cols, rows=rows, color1=color1, color2=color2)

if __name__ == '__main__':
    app.run(debug=True)