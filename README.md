# Daily-Diet-API
Criação de API em Flask para o backend de um sistema de dieta diária

## 🚀 Começando

Para ter uma cópia do projeto em sua máquina local basta abrir seu terminal e digitar o comando para clonar, junto da url do projeto.

```
git clone https://github.com/Almeedus/Daily-Diet-API.git
```

### 📋 Pré-requisitos

- Python 3.12.2
- Docker 20.10.24
- Docker-compose 1.29.2

### 🔧 Instalação

Com o python3 instalado localmente em sua maquina, abra o diretório do projeto e baixe as bibliotecas que são obrigatórias para o funcionamento do projeto. Para isso siga o seguinte comando.

```
pip3 install -r requirements.txt
```

Após a instalação de todos os requisitos obrigatórios para o projeto, rode o docker-compose para iniciar o container do MySQL:

Atenção: para realizar o comando a seguir, certifique-se de estar no diretório do projeto, pois o comando irá buscar pelo docker-compose.yml

```
docker-compose.yml
```

Para configurar o banco de dados iremos utilizar o comando do terminal do flask
```
flask shell
```

Dentro do flask shell seguiremos com os seguintes comandos para criar o banco de dados
```
db.create_all()
```

E por fim salvar as mudanças realizadas anteriormente
```
db.session.commit()
```

Pronto, agora é só sair do terminal do flask
```
exit()
```


## ⚙️ Executando os testes

Inicie o módulo criado com o comando
```
python3 app.py
```

### 🔩 Analise os testes de ponta a ponta

Configure os endpoints em seu software de consumo de API de preferencia.

```
Dar exemplos
```

## 🛠️ Construído com

* [Python](https://docs.python.org/3/) - Linguagem utilizada
* [Flask](https://docs.python.org/3/) - Framework utilizado
* [Docker](https://docs.docker.com/) - Usado para gerar o container de MySQL
* [MySQL](https://dev.mysql.com/doc/) - Banco de Dados utilizado
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/) - Extensão para o FLask para dar suporte ao SQL na aplicação.
* [Werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/) - Biblioteca abrangente de aplicativos da web WSGI.
* [Pymysql](https://pymysql.readthedocs.io/en/latest/) - Usado para criar o banco de dados.