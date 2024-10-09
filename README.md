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
