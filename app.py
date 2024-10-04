from flask import Flask, jsonify, request
import requests
from flask_sqlalchemy import SQLAlchemy
from mysql.connector import (connection)
from datetime import date
import mysql.connector

app = Flask(__name__)

SWAPI_BASE_URL = "https://swapi.dev/api/"

# Função para conectar com o banco
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

# Endpoint para verificar status
@app.route('/', methods=['GET'])
def home():
    return jsonify("ok")

# Endpoint para listar personagens
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

@app.route('/personagens/<int:id>/delete', methods=['GET', 'DELETE'])
def delete_personagem(id):
    connection = create_connection()

    sql = "DELETE FROM personagens WHERE id = %s"
    
    cursor = connection.cursor()
    cursor.execute(sql, (id,))
        
    connection.commit()

    return jsonify({"message": "Personagem excluído com sucesso!"}), 200

# Endpoint para listar planetas
@app.route('/planetas', methods=['GET'])
def get_planets():
    data = get_swapi_data('planets/')
    return jsonify(data)

@app.route('/planetas/<int:id>', methods=['GET'])
def get_planets_by_id(id):
    data = get_swapi_data(f'planets/{id}/')
    return jsonify(data)

@app.route('/planetas/<int:id>/save', methods=['GET', 'POST'])
def add_planeta(id):
    connection = create_connection()

    swapi_data = get_swapi_data(f'planets/{id}/')
    
    sql = "INSERT INTO planetas (id, nome, clima, diametro, gravidade, periodo_orbita, populacao, periodo_rotacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (id, swapi_data.get('name'), swapi_data.get('climate'), swapi_data.get('diameter'), swapi_data.get('gravity'), swapi_data.get('orbital_period'),
              swapi_data.get('population'), swapi_data.get('rotation_period'))

    cursor = connection.cursor()
    cursor.execute(sql, values)
        
    connection.commit()

    return jsonify({"message": "Planeta adicionado com sucesso!"}), 201

@app.route('/planetas/<int:id>/delete', methods=['GET', 'DELETE'])
def delete_planeta(id):
    connection = create_connection()

    sql = "DELETE FROM planetas WHERE id = %s"
    
    cursor = connection.cursor()
    cursor.execute(sql, (id,))
        
    connection.commit()

    return jsonify({"message": "Planeta excluído com sucesso!"}), 200

# Endpoint para listar naves
@app.route('/naves', methods=['GET'])
def get_starships():
    data = get_swapi_data('starships/')
    return jsonify(data)

@app.route('/naves/<int:id>', methods=['GET'])
def get_starships_by_id(id):
    data = get_swapi_data(f'starships/{id}/')
    return jsonify(data)

@app.route('/naves/<int:id>/save', methods=['GET', 'POST'])
def add_naves(id):
    connection = create_connection()

    swapi_data = get_swapi_data(f'starships/{id}/')
    
    sql = "INSERT INTO naves (id, nome, custo, passageiros) VALUES (%s, %s, %s, %s)"
    values = (id, swapi_data.get('name'), swapi_data.get('cost_in_credits'), swapi_data.get('passengers'))

    cursor = connection.cursor()
    cursor.execute(sql, values)
        
    connection.commit()

    return jsonify({"message": "Nave adicionada com sucesso!"}), 201

@app.route('/naves/<int:id>/delete', methods=['GET', 'DELETE'])
def delete_nave(id):
    connection = create_connection()

    sql = "DELETE FROM naves WHERE id = %s"
    
    cursor = connection.cursor()
    cursor.execute(sql, (id,))
        
    connection.commit()

    return jsonify({"message": "Nave excluída com sucesso!"}), 200

# Endpoint para listar filmes
@app.route('/filmes', methods=['GET'])
def get_films():
    data = get_swapi_data('films/')
    return jsonify(data)

@app.route('/filmes/<int:id>', methods=['GET'])
def get_films_by_id(id):
    data = get_swapi_data(f'films/{id}/')
    return jsonify(data)

@app.route('/filmes/<int:id>/save', methods=['GET', 'POST'])
def add_filme(id):
    connection = create_connection()

    swapi_data = get_swapi_data(f'films/{id}/')
    
    sql = "INSERT INTO filmes (id, nome, diretor, episodio) VALUES (%s, %s, %s, %s)"
    values = (id, swapi_data.get('title'), swapi_data.get('director'), swapi_data.get('episode_id'))

    cursor = connection.cursor()
    cursor.execute(sql, values)
        
    connection.commit()

    return jsonify({"message": "Filme adicionado com sucesso!"}), 201

@app.route('/filmes/<int:id>/delete', methods=['GET', 'DELETE'])
def delete_filme(id):
    connection = create_connection()

    sql = "DELETE FROM filmes WHERE id = %s"
    
    cursor = connection.cursor()
    cursor.execute(sql, (id,))
        
    connection.commit()

    return jsonify({"message": "Filme excluído com sucesso!"}), 200

# Endpoint para listar veículos
@app.route('/veiculos', methods=['GET'])
def get_vehicles():
    data = get_swapi_data('vehicles/')
    return jsonify(data)

@app.route('/veiculos/<int:id>', methods=['GET'])
def get_vehicles_by_id(id):
    data = get_swapi_data(f'vehicles/{id}/')
    return jsonify(data)

@app.route('/veiculos/<int:id>/save', methods=['GET', 'POST'])
def add_veiculo(id):
    connection = create_connection()

    swapi_data = get_swapi_data(f'vehicles/{id}/')
    
    sql = "INSERT INTO veiculos (id, nome, modelo, passageiros) VALUES (%s, %s, %s, %s)"
    values = (id, swapi_data.get('name'), swapi_data.get('model'), swapi_data.get('passengers'))

    cursor = connection.cursor()
    cursor.execute(sql, values)
        
    connection.commit()

    return jsonify({"message": "Veículo adicionado com sucesso!"}), 201

@app.route('/veiculos/<int:id>/delete', methods=['GET', 'DELETE'])
def delete_veiculo(id):
    connection = create_connection()

    sql = "DELETE FROM veiculos WHERE id = %s"
    
    cursor = connection.cursor()
    cursor.execute(sql, (id,))
        
    connection.commit()

    return jsonify({"message": "Veículo excluído com sucesso!"}), 200

# Endpoint para listar espécies
@app.route('/especies', methods=['GET'])
def get_species():
    data = get_swapi_data('species/')
    return jsonify(data)

@app.route('/especies/<int:id>', methods=['GET'])
def get_species_by_id(id):
    data = get_swapi_data(f'species/{id}/')
    return jsonify(data)

@app.route('/especies/<int:id>/save', methods=['GET', 'POST'])
def add_especie(id):
    connection = create_connection()

    swapi_data = get_swapi_data(f'species/{id}/')
    
    sql = "INSERT INTO especies (id, nome, lingua, classificacao) VALUES (%s, %s, %s, %s)"
    values = (id, swapi_data.get('name'), swapi_data.get('language'), swapi_data.get('classification'))

    cursor = connection.cursor()
    cursor.execute(sql, values)
        
    connection.commit()

    return jsonify({"message": "Espécie adicionada com sucesso!"}), 201

@app.route('/especies/<int:id>/delete', methods=['GET', 'DELETE'])
def delete_especie(id):
    connection = create_connection()

    sql = "DELETE FROM especies WHERE id = %s"
    
    cursor = connection.cursor()
    cursor.execute(sql, (id,))
        
    connection.commit()

    return jsonify({"message": "Espécie excluída com sucesso!"}), 200


# Rota para salvar os favoritos no banco de dados
@app.route('/favorito/save', methods=['GET', 'POST'])
def save_favorito():
    connection = create_connection()
    cursor = connection.cursor()

    personagem = get_swapi_data("people/1/")
    filme = get_swapi_data("films/6/")
    nave = get_swapi_data("starships/10/")
    veiculo = get_swapi_data("vehicles/14/")
    especie = get_swapi_data("species/1/")
    planeta = get_swapi_data("planets/1/")

    sql = """
        INSERT INTO favorito (personagem_nome, personagem_ano_nascimento, filme_nome, filme_numero, nave_nome, nave_modelo,
        veiculo_nome, veiculo_modelo, especie_planeta_natal, especie_linguas, planeta_nome, planeta_populacao)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        personagem['name'],
        personagem['birth_year'],
        filme['title'],
        filme['episode_id'],
        nave['name'],
        nave['model'],
        veiculo['name'],
        veiculo['model'],
        especie['homeworld']['name'],
        ", ".join(especie['language']),
        planeta['name'],
        planeta['population']
    )

    cursor.execute(sql, values)
    connection.commit()

    return jsonify({"message": "Favoritos salvo com sucesso!"}), 201

# Rota para buscar os favoritos
@app.route('/getFavorito', methods=['GET'])
def get_favorito():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM favorito LIMIT 1")
    favorito = cursor.fetchone()

    if favorito:
        
        planeta_natal_especie = get_swapi_data(favorito[9])

        response = {
            "personagem_nome": favorito[1],
            "personagem_ano_nascimento": favorito[2],
            "filme_nome": favorito[3],
            "filme_numero": favorito[4],
            "nave_nome": favorito[5],
            "nave_modelo": favorito[6],
            "veiculo_nome": favorito[7],
            "veiculo_modelo": favorito[8],
            "especie_planeta_natal": favorito[9],
            "especie_linguas": favorito[10],
            "planeta_nome": favorito[11],
            "planeta_populacao": favorito[12],
            "alunos": [
                {
                    "nome": "Luiz Felipe",
                    "matricula": "98021809"
                },
                {
                    "nome": "Bruno Almeida",
                    "matricula": "98021376"
                },
                {
                    "nome": "Matheus Rezende",
                    "matricula": "98021793"
                }
            ],
            "curso": "Sistemas de Informação",
            "universidade": "Univas",
            "periodo": "Sexto período"
        }
        return jsonify(response), 200
    else:
        return jsonify({"message": "Nenhum favorito encontrado!"}), 404

@app.route('/favoritos', methods=['GET'])
def get_favorites():
    data = get_swapi_data('species/')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
