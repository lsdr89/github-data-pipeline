# Pipeline de Dados GitHub → PostgreSQL

## Objetivo

Este projeto foi criado com o objetivo de estudar os conceitos fundamentais de Engenharia de Dados.

A aplicação realiza a coleta de informações de repositórios do GitHub através da API pública da plataforma, processa os dados recebidos e armazena as informações em um banco de dados PostgreSQL.

Durante o desenvolvimento deste projeto foram praticados conceitos como:

* Consumo de APIs REST
* Manipulação de dados JSON
* Programação em Python
* Banco de Dados PostgreSQL
* SQL
* Docker
* ETL (Extract, Transform, Load)
* Versionamento com Git e GitHub

---

## Arquitetura do Projeto

```text
GitHub API
    ↓
Python
    ↓
PostgreSQL
    ↓
Consultas SQL
```

---

## Tecnologias Utilizadas

### Linguagem

* Python 3

### Bibliotecas

* requests
* psycopg2-binary
* pandas

### Banco de Dados

* PostgreSQL 16

### Containers

* Docker
* Docker Compose

### Versionamento

* Git
* GitHub

---

## Estrutura do Projeto

```text
github-data-pipeline/

├── docker-compose.yml
├── github_test.py
├── extract.py
├── connect.py
├── load.py
├── .gitignore
└── README.md
```

---

## Etapas do Pipeline

### 1. Extração (Extract)

Nesta etapa o Python realiza uma requisição para a API do GitHub buscando repositórios relacionados ao termo:

```text
data-engineering
```

Os dados retornam em formato JSON.

Exemplo de informações coletadas:

* Nome do repositório
* Quantidade de estrelas
* Quantidade de forks
* Linguagem principal utilizada

---

### 2. Transformação (Transform)

Os dados recebidos da API são processados pelo Python.

Nesta etapa são selecionados apenas os campos necessários para armazenamento no banco de dados.

---

### 3. Carga (Load)

Após o tratamento dos dados, as informações são gravadas na tabela PostgreSQL.

Estrutura da tabela:

```sql
CREATE TABLE repositories (

    id SERIAL PRIMARY KEY,

    repo_name VARCHAR(200),

    stars INTEGER,

    forks INTEGER,

    language VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
```

---

## Como Executar

### Subir o PostgreSQL

```bash
docker compose up -d
```

Verificar se o container está em execução:

```bash
docker ps
```

---

### Criar ambiente virtual Python

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Instalar dependências

```bash
pip install requests
pip install psycopg2-binary
pip install pandas
```

---

### Executar a carga dos dados

```bash
python load.py
```

---

## Validação

Acessar o PostgreSQL:

```bash
docker exec -it <container_id> psql -U admin githubdb
```

Consultar os registros inseridos:

```sql
SELECT *
FROM repositories;
```

---

## O que Aprendi com este Projeto

Durante o desenvolvimento deste projeto aprendi:

* Como consumir uma API utilizando Python.
* Como interpretar respostas JSON.
* Como conectar Python ao PostgreSQL.
* Como inserir registros utilizando SQL.
* Como utilizar Docker para disponibilizar bancos de dados rapidamente.
* Como versionar código utilizando Git.
* Como publicar projetos no GitHub.

---

## Próximos Passos

Planejo evoluir este projeto adicionando:

* Tratamento de erros
* Logs de execução
* Variáveis de ambiente (.env)
* Docker para a aplicação Python
* Apache Airflow
* DBT
* Data Warehouse
* Dashboard Power BI
* Integração com AWS

---
