# checklist_api# Checklist API

![pipeline](https://github.com/zpaulo/checklist_api/actions/workflows/pipeline.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.13-blue)
![Framework](https://img.shields.io/badge/framework-FastAPI-green)
![Database](https://img.shields.io/badge/database-PostgreSQL-blueviolet)

Uma API de lista de tarefas (Checklist) desenvolvida com FastAPI, SQLAlchemy e PostgreSQL, utilizando as melhores práticas de desenvolvimento como testes automatizados e CI/CD.

## ✨ Features

- **Autenticação de Usuários**: Sistema completo de registro e login com tokens JWT.
- **Gerenciamento de Usuários (CRUD)**: Crie, leia, atualize e delete usuários de forma segura.
- **Gerenciamento de Tarefas (CRUD)**: Crie, leia, atualize e delete tarefas associadas a cada usuário.
- **Filtros e Paginação**: Suporte para filtrar e paginar listas de tarefas e usuários.
- **Estrutura Assíncrona**: Totalmente assíncrona para alta performance.
- **Containerização**: Fácil de rodar e escalar com Docker e Docker Compose.
- **Migrações de Banco de Dados**: Gerenciamento de schema com Alembic.
- **Testes Automatizados**: Cobertura de testes completa para garantir a estabilidade da aplicação.
- **Pipeline de CI/CD**: Integração contínua configurada com GitHub Actions.

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

- **Backend**: FastAPI, Pydantic, SQLAlchemy (com asyncio)
- **Banco de Dados**: PostgreSQL
- **Autenticação**: JWT (PyJWT), Pwdlib
- **Testes**: Pytest, Pytest-asyncio, Factory-Boy, Testcontainers
- **Containerização**: Docker, Docker Compose
- **Migrações**: Alembic
- **Runner de Tarefas**: Taskipy
- **CI/CD**: GitHub Actions

## 🚀 Como Começar

Para executar o projeto localmente, você precisará ter o **Docker** e o **Docker Compose** instalados.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/checklist_api.git](https://github.com/seu-usuario/checklist_api.git)
    cd checklist_api
    ```

2.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto, baseado no `checklist_api/settings.py`. Ele deve conter as seguintes variáveis:
    ```env
    DATABASE_URL=postgresql+psycopg://app_user:app_password@checklistapi_database:5432/app_db
    SECRET_KEY=sua_chave_secreta_super_segura
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```
    > 🔑 **Dica**: Você pode gerar uma `SECRET_KEY` forte usando `openssl rand -hex 32` no seu terminal.

3.  **Inicie os containers:**
    Use o Docker Compose para construir as imagens e iniciar os serviços da API e do banco de dados.
    ```bash
    docker-compose up --build
    ```

4.  **Acesse a API:**
    A aplicação estará disponível em `http://localhost:8000`. A documentação interativa (Swagger UI) pode ser acessada em `http://localhost:8000/docs`.

## 🧪 Rodando os Testes

O projeto utiliza `taskipy` para facilitar a execução de tarefas comuns, como rodar os testes. Para executar a suíte de testes, use o comando:

```bash
poetry run task test


Sim, a melhor forma é exatamente copiar o conteúdo e colar no seu arquivo README.md no GitHub.

Para garantir que a formatação fique perfeita, vou te entregar o conteúdo completo dentro de um bloco de código. Assim, você pode clicar em "Copiar" e colar diretamente, sem perder nenhuma formatação do Markdown.

Como Fazer
Vá para a página principal do seu repositório no GitHub.

Encontre o arquivo README.md e clique no ícone de lápis (✏️) para editá-lo.

Apague todo o conteúdo antigo.

Copie o bloco de código abaixo e cole no campo de edição do GitHub.

Clique em "Commit changes..." para salvar.

Aqui está o código pronto para copiar e colar:

Markdown

# Checklist API

![pipeline](https://github.com/zpaulo/checklist_api/actions/workflows/pipeline.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.13-blue)
![Framework](https://img.shields.io/badge/framework-FastAPI-green)
![Database](https://img.shields.io/badge/database-PostgreSQL-blueviolet)

Uma API de lista de tarefas (Checklist) desenvolvida com FastAPI, SQLAlchemy e PostgreSQL, utilizando as melhores práticas de desenvolvimento como testes automatizados e CI/CD.

## ✨ Features

- **Autenticação de Usuários**: Sistema completo de registro e login com tokens JWT.
- **Gerenciamento de Usuários (CRUD)**: Crie, leia, atualize e delete usuários de forma segura.
- **Gerenciamento de Tarefas (CRUD)**: Crie, leia, atualize e delete tarefas associadas a cada usuário.
- **Filtros e Paginação**: Suporte para filtrar e paginar listas de tarefas e usuários.
- **Estrutura Assíncrona**: Totalmente assíncrona para alta performance.
- **Containerização**: Fácil de rodar e escalar com Docker e Docker Compose.
- **Migrações de Banco de Dados**: Gerenciamento de schema com Alembic.
- **Testes Automatizados**: Cobertura de testes completa para garantir a estabilidade da aplicação.
- **Pipeline de CI/CD**: Integração contínua configurada com GitHub Actions.

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

- **Backend**: FastAPI, Pydantic, SQLAlchemy (com asyncio)
- **Banco de Dados**: PostgreSQL
- **Autenticação**: JWT (PyJWT), Pwdlib
- **Testes**: Pytest, Pytest-asyncio, Factory-Boy, Testcontainers
- **Containerização**: Docker, Docker Compose
- **Migrações**: Alembic
- **Runner de Tarefas**: Taskipy
- **CI/CD**: GitHub Actions

## 🚀 Como Começar

Para executar o projeto localmente, você precisará ter o **Docker** e o **Docker Compose** instalados.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/checklist_api.git](https://github.com/seu-usuario/checklist_api.git)
    cd checklist_api
    ```

2.  **Configure as variáveis de ambiente:**
    Crie um arquivo `.env` na raiz do projeto, baseado no `checklist_api/settings.py`. Ele deve conter as seguintes variáveis:
    ```env
    DATABASE_URL=postgresql+psycopg://app_user:app_password@checklistapi_database:5432/app_db
    SECRET_KEY=sua_chave_secreta_super_segura
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```
    > 🔑 **Dica**: Você pode gerar uma `SECRET_KEY` forte usando `openssl rand -hex 32` no seu terminal.

3.  **Inicie os containers:**
    Use o Docker Compose para construir as imagens e iniciar os serviços da API e do banco de dados.
    ```bash
    docker-compose up --build
    ```

4.  **Acesse a API:**
    A aplicação estará disponível em `http://localhost:8000`. A documentação interativa (Swagger UI) pode ser acessada em `http://localhost:8000/docs`.

## 🧪 Rodando os Testes

O projeto utiliza `taskipy` para facilitar a execução de tarefas comuns, como rodar os testes. Para executar a suíte de testes, use o comando:

```bash
poetry run task test
Este comando irá executar todos os testes automatizados e exibir um relatório de cobertura de código.

📁 Estrutura do Projeto
checklist_api/
├── .github/workflows/      # Pipeline de CI/CD com GitHub Actions
├── alembic.ini             # Configuração do Alembic
├── migrations/             # Scripts de migração do banco de dados
├── tests/                  # Testes automatizados
├── checklist_api/
│   ├── routers/            # Módulos de rotas da API (auth, users, todos)
│   ├── database.py         # Configuração da conexão com o banco de dados
│   ├── models.py           # Modelos de dados do SQLAlchemy
│   ├── schemas.py          # Schemas Pydantic para validação de dados
│   ├── security.py         # Lógica de autenticação e segurança
│   ├── settings.py         # Configurações da aplicação
│   └── main.py             # Ponto de entrada da aplicação FastAPI
├── compose.yaml            # Configuração do Docker Compose
├── Dockerfile              # Instruções para construir a imagem Docker da API
├── entrypoint.sh           # Script de inicialização do container
└── pyproject.toml          # Definição do projeto e dependências

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para relatar bugs ou sugerir novas funcionalidades. Se desejar contribuir com código, por favor, faça um fork do repositório e envie um Pull Request.