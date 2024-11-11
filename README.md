Aqui está a resolução do desafio da API REST.
Neste desafio desenvolvir praticas de Python com o framework Django Ninja
Para testar em sua maquina é necessário clonar o repositório.
Logo em seguida, siga estes passos!
Passo 1: Abra seu terminal cmd no local do arquivo da API
Passo 2: Execute o seguinte comando para iniciar em sua maquina local: python manage.py runserver
Passo 3: Se necessário, instale o framework django ninja em sua máquina
Passo 4: Cole a URL que o terminal ira lhe oferecer.
Passo 5: Nesta http://127.0.0.1:8000/ que apareceu em minha máquina adicone ao final da URL http://127.0.0.1:8000/admin
Passo 6: Irá cair na tela de login: Digite em Username: gabriel; em password: 1234.
Assim poderá acessar a área do admin da API e assim testar todas as funções da API.
Caso queira acessar a documentação, entre com o seguinte link: http://127.0.0.1:8000/cliente/api/v1/docs#/
Para acessar as outras duas startapp acesse o seguinte codigo para pedido: http://127.0.0.1:8000/pedido/api/v2/docs#/
Para acessar as outras duas startapp acesse o seguinte codigo para itens_pedido: http://127.0.0.1:8000/itens_pedido/api/v3/docs#/
A seguir o codigo do banco de dados em mysql:

CREATE DATABASE desafio;
USE desafio;

CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);


CREATE TABLE pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    total DECIMAL(12,2) NOT NULL,
    status VARCHAR(15) NOT NULL,
    date_pedido DATE NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES cliente(id)
);


CREATE TABLE itens_pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    nome VARCHAR(90) NOT NULL,
    descricao VARCHAR(130) NOT NULL,
    preco DECIMAL(12,2) NOT NULL,
    categoria VARCHAR(20),
    FOREIGN KEY (pedido_id) REFERENCES pedido(id)
);
OBS: Não conseguir conectar a API ao banco de dados(Se tivesse um pouco mais de tempo, estudaria mais e resolveria o problema), 
mais assistir algumas aulas antigas e fiz o codigo para que funcionasse em mysql.
API DESAFIO: Desenvolvido por Gabriel Mazulo.
