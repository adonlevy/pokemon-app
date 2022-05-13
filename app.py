from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/kanto', methods=['GET'])
def kanto():
    return render_template('region.html', region="Kanto")


@app.route('/johto', methods=['GET'])
def johto():
    return render_template('region.html', region="Johto")


if __name__ == '__main__':
    app.run(debug=True)
