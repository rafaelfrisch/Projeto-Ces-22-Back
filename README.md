# Projeto CES-22 BackEnd

Este repositório consiste do código responsável pelo funcionamento do back-end do projeto de CES-22, API REST desenvolvida com Django e Django-rest-framework.


## Estruturação do Projeto

- /app
    - /admin
    - /models
    - /serializers
    - /tests
    - /urls
    - /views

- requirements.txt (nesse arquivo, fica-se todos as bibliotecas necessárias para rodar o back-end)

### Não subam, em momento nenhum, algum __\_\_pycache\_\___ , __ambiente virtual__ , .idea ou __migrations__!!


## SETUP

### Criar Ambiente virtual no python
  ```
  virtualenv venv
  ```

### Acessar Ambiente virtual no Windows
  ```
  cd venv/Scripts/
  ./activate
  ```

### Acessar Ambiente virtual no Ubuntu
  ```
  source venv/bin/activate
  ```

### Instalação de dependências do projeto (Listadas no arquivo requirements.txt)
  ```
  pip install -r requirements.txt
  ```
#### Lembre-se de entrar no ambiente virtual antes de instalar as dependências

### Instalação de novas dependências
  ```
  pip install <nome_da_dependencia>
  ```
#### Atualizar o arquivo requirements.txt (Dentro do ambiente Virtual)
  ```
  pip freeze > requirements.txt
  ```

### Instalação de dependências do projeto (Listadas no arquivo requirements.txt)
  ```
  pip install -r requirements.txt
  ```
  
### Configuração do Bando de Dados(Postgres)
- Abrir o Postgres:
    - Caso esteja no windows:
      ```
      psql -U postgres
      ```
	- Caso esteja no linux:
      ```
      sudo -u postgres psql
      ```
- Criar um usuário:
  ```
  CREATE USER ces22 WITH PASSWORD 'projeto';
  ```
- Criar o DB:
  ```
  CREATE DATABASE dbces22 WITH OWNER ces22;
  ```

### Caso seja necessário, recrie o DB
  ```
  DROP DATABASE dbces22;
  CREATE DATABASE dbces22 WITH OWNER ces22;
  ```

### Rodar a aplicação
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Para criar dados automaticamente, acesse essa url  
```
localhost:8000/data/generate_data/
```

### Caso queira acessar o django-admin, acesse essa url
```
localhost:8000/admin/
```

### Usuarios criados pelo generate_data

#### Superusuario
```
email - usuario_admin@gmail.com
senha - 123456
```

## Padronizações
### Nome de apps

Os apps devem ser nomeados em __snake case__, __inglês__ sem __nenhum maiúsculo__ , como no seguinte padrão:

`name_of_app`

### Nome de variáveis

Todos as variáveis devem ser nomeados em __snake case__, __inglês__ sem __nenhum maiúsculo__, como no seguinte padrão:

`name_of_variable`
### Nome de Funções

Todos as funções devem ser nomeados em __snake case__, __inglês__ como no seguinte padrão:

`name_of_function`
### Nome de classe

Todos as classes devem ser nomeados em __snake case__, __português__ com apenas a __primeira letra da função maiúscula__, como no seguinte padrão:

`Nome_da_classe`
## Nome de branch

Todas as branch devem ser nomeados em __snake case__, __minúsculo__ e em __inglês__ como no seguinte padrão:

`name_of_branch`
## Banco de Dados

O banco de dados utilizado é o [PostgreSQL](https://www.postgresql.org/).
