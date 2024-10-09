Para a execução do trabalho foi utilizada a linguagem Python juntamente com o banco de dados MySQL para o armazenamento das informações.

- Quando bater na rota “/personagens”, retorna um arquivo json de todos os personagens disponíveis na API.
  
- Quando bater na rota “/filmes”, retorna um arquivo json de todos os filmes disponíveis na API.
  
- Quando bater na rota “/naves”, retorna um arquivo json de todos as naves disponíveis na API.
  
- Quando bater na rota “/veiculos”, retorna um arquivo json de todos os veiculos disponíveis na API.
  
- Quando bater na rota “/especies”, retorna um arquivo json de todos os especies disponíveis na API.
  
- Quando bater na rota “/planetas”, retorna um arquivo json de todos os planetas disponíveis na API.
  
- Quando bater na rota “/favoritos”, retorna um arquivo json de todos objetos que foram favoritados.

Ao acessar a rota "/objeto/save", salva o objeto no banco de dados e o mesmo é consultado através da rota "/favoritos".

Ao acessar a rota "objeto/delete", exclui o objeto do banco de dados e o mesmo não estará mais disponível para a consulta através da rota "/favoritos".


Para a execução do projeto precisa criar um banco de dados no MySQL:

Usuário = "root";
Senha = "123456";
Nome do banco: "StarWars"

E executar o seguinte script:

create table personagens (
	id int(3),
	nome varchar(100),
	genero varchar(6),
	primary key (id)
);

create table planetas (
	id int(3),
	nome varchar(100),
	clima varchar(100),
	diametro int(10),
	gravidade int(10),
	periodo_orbita int(10),
	populacao int(10),
	periodo_rotacao int(10),
	primary key (id)
);

create table naves (
	id int(3),
	nome varchar(100),
	custo int(10),
	passageiros int(10),
	primary key (id)
);

create table filmes (
	id int(3),
	nome varchar(100),
	diretor varchar(100),
	episodio int(3),
	primary key (id)
);

create table veiculos (
	id int(3),
	nome varchar(100),
	modelo varchar(100),
	primary key (id)
);

create table especies (
	id int(3),
	nome varchar(100),
	classificacao varchar(100),
	primary key (id)
);

create table favorito (
	id int NOT NULL DEFAULT 1,
	personagem_nome varchar(30) not null,
	personagem_ano_nascimento varchar(10),
	filme_nome varchar(30),
	filme_numero int(3),
	nave_nome varchar(30),
	nave_modelo varchar(30),
	veiculo_nome varchar(30),
	veiculo_modelo varchar(30),
	especie_planeta_natal varchar(40),
	especie_linguas varchar(100),
	planeta_nome varchar(30),
	planeta_populacao int(10),
	primary key (id)
);
