from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

SWAPI_BASE_URL = "https://swapi.dev/api/"

# Função para buscar dados da SWAPI
def get_swapi_data(endpoint):
    response = requests.get(SWAPI_BASE_URL + endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Não foi possível obter dados da SWAPI"}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/personagens', methods=['GET'])
def get_characters():
    data = get_swapi_data('people/')
    return jsonify(data)


@app.route('/personagens/<int:id>', methods=['GET'])
def get_character_by_id(id):
    data = get_swapi_data(f'people/{id}/')
    return jsonify(data)

# Endpoint para listar planetas
@app.route('/planetas', methods=['GET'])
def get_planets():
    data = get_swapi_data('planets/')
    return jsonify(data)

@app.route('/planetas/<int:id>', methods=['GET'])
def get_planets_by_id(id):
    data = get_swapi_data(f'planets/{id}/')
    return jsonify(data)

# Endpoint para listar naves
@app.route('/naves', methods=['GET'])
def get_starships():
    data = get_swapi_data('starships/')
    return jsonify(data)

@app.route('/naves/<int:id>', methods=['GET'])
def get_starships_by_id(id):
    data = get_swapi_data(f'starships/{id}/')
    return jsonify(data)

# Endpoint para listar personagens
@app.route('/filmes', methods=['GET'])
def get_films():
    data = get_swapi_data('films/')
    return jsonify(data)

@app.route('/filmes/<int:id>', methods=['GET'])
def get_films_by_id(id):
    data = get_swapi_data(f'films/{id}/')
    return jsonify(data)

# Endpoint para listar personagens
@app.route('/veiculos', methods=['GET'])
def get_vehicles():
    data = get_swapi_data('vehicles/')
    return jsonify(data)

@app.route('/veiculos/<int:id>', methods=['GET'])
def get_vehicles_by_id(id):
    data = get_swapi_data(f'vehicles/{id}/')
    return jsonify(data)

# Endpoint para listar personagens
@app.route('/especies', methods=['GET'])
def get_species():
    data = get_swapi_data('species/')
    return jsonify(data)

@app.route('/especies/<int:id>', methods=['GET'])
def get_species_by_id(id):
    data = get_swapi_data(f'species/{id}/')
    return jsonify(data)

@app.route('/favoritos', methods=['GET'])
def get_favorites():
    data = get_swapi_data('species/')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
