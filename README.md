# Documentação da API FastAPI

Esta é uma API para gerenciamento de estoque, permitindo adicionar, remover e atualizar produtos, além de gerar relatórios.

## Estrutura do Projeto

app/
│
├── database/
│   └── ...
│
├── services/
│   ├── estoque_service.py
│   └── ...
│
└── main.py

## Endpoints

### 1. Adicionar Produto

- **Método:** `POST`
- **URL:** `/adicionar`
- **Descrição:** Adiciona um novo produto ao estoque.

#### Parâmetros

| Nome          | Tipo    | Descrição                        |
|---------------|---------|----------------------------------|
| `produto_id`  | `int`   | ID do produto                   |
| `nome`        | `str`   | Nome do produto                 |
| `preco`       | `float` | Preço do produto                |
| `quantidade`  | `int`   | Quantidade do produto a ser adicionado |

#### Resposta
- Retorna os detalhes do produto adicionado.

---

### 2. Remover Produto

- **Método:** `POST`
- **URL:** `/remover`
- **Descrição:** Remove uma quantidade específica de um produto do estoque.

#### Parâmetros

| Nome          | Tipo    | Descrição                        |
|---------------|---------|----------------------------------|
| `produto_id`  | `int`   | ID do produto                   |
| `quantidade`  | `int`   | Quantidade do produto a ser removida |

#### Resposta
- Retorna os detalhes do produto após a remoção.

---

### 3. Atualizar Estoque

- **Método:** `PUT`
- **URL:** `/atualizar`
- **Descrição:** Atualiza a quantidade de um produto no estoque.

#### Parâmetros

| Nome          | Tipo    | Descrição                        |
|---------------|---------|----------------------------------|
| `produto_id`  | `int`   | ID do produto                   |
| `quantidade`  | `int`   | Nova quantidade do produto       |

#### Resposta
- Retorna os detalhes do produto após a atualização.

---

### 4. Gerar Relatório

- **Método:** `GET`
- **URL:** `/relatorio`
- **Descrição:** Gera um relatório com informações sobre os produtos em estoque.

#### Resposta
- Retorna um relatório formatado dos produtos em estoque.

---

## Como Executar

1. Clone o repositório:
   git clone <url-do-repositorio>
   cd <diretorio-do-repositorio>

2. Instale as dependências:
   pip install -r requirements.txt

3. Execute a aplicação:
   uvicorn app.main:app --reload

A API estará disponível em `http://127.0.0.1:8000`.

## Testando a API

Você pode usar ferramentas como [Postman](https://www.postman.com/) ou [curl](https://curl.se/) para testar os endpoints.
