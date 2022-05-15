from flask import Flask, render_template, request
from helpers import get_pokemon, search_pokemon

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gen1', methods=['GET'])
def region():
    if request.method == 'GET':
        pokemon = get_pokemon(151, 1)
        return render_template('region.html', region="Generation 1", pokemon=pokemon)


@app.route('/gen2', methods=['GET'])
def johto():
    if request.method == 'GET':
        pokemon = get_pokemon(251, 2)
        return render_template('region.html', region="Generation 2", pokemon=pokemon)


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        name = request.form.get("name")
        pokemon = search_pokemon(name)
        if pokemon is None:
            return render_template('error.html', message="pokemon doesn't exist")
        else:
            return render_template('search.html', pokemon=pokemon)


if __name__ == '__main__':
    app.run(debug=True)
