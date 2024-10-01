from flask import Flask, jsonify, request
import requests
from flask_sqlalchemy import SQLAlchemy
from mysql.connector import (connection)
from datetime import date
import mysql.connector

app = Flask(__name__)

SWAPI_BASE_URL = "https://swapi.dev/api/"

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',         # Seu nome de usuário
            password='123456',   # Sua senha
            database='StarWars'  # Nome do seu banco de dados
        )
        print("Conexão com o MySQL bem-sucedida")
    except Error as e:
        print(f"Erro '{e}' ocorreu")
    return connection

# Função para buscar dados da SWAPI
def get_swapi_data(endpoint):
    response = requests.get(SWAPI_BASE_URL + endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Não foi possível obter dados da SWAPI"}


@app.route('/', methods=['GET'])
def home():
    return jsonify("ok")


@app.route('/personagens', methods=['GET'])
def get_characters():
    data = get_swapi_data('people/')
    return jsonify(data)


@app.route('/personagens/<int:id>', methods=['GET'])
def get_character_by_id(id):
    data = get_swapi_data(f'people/{id}/')
    return jsonify(data)

@app.route('/personagens/<int:id>/save', methods=['GET', 'POST'])
def add_personagem(id):
    connection = create_connection()

    swapi_data = get_swapi_data(f'people/{id}/')
    
    sql = "INSERT INTO personagens (id, nome, genero) VALUES (%s, %s, %s)"
    values = (id, swapi_data.get('name'), swapi_data.get('gender'))

    cursor = connection.cursor()
    cursor.execute(sql, values)
        
    connection.commit()

    return jsonify({"message": "Personagem adicionado com sucesso!"}), 201

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
