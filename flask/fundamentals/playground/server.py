from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
@app.route('/play/<times>')
@app.route('/play/<times>/<color>')
def squares(times=3, color='blue'):
    times = int(times)
    color = str(color)
    return render_template('index.html', times=times, color=color)

if __name__ == '__main__':
    app.run(debug=True)