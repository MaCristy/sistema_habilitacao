## Sistema de Habilitações

O Sistema de Habilitações é uma API desenvolvida em Python + Flask para gerenciar cadastros de habilitações (CNH).
O objetivo é permitir que aplicações externas possam criar, listar, atualizar e excluir habilitações de maneira simples e organizada.
Esse projeto foi criado para fins de estudo e prática de construção de APIs REST.

## 🛠️Tecnologias Utilizadas

* **Python 3.12.3:** Linguagem principal do projeto, usada para construção de toda a lógica da API.
* **Flask:** Framework web leve e rápido usado para criar as rotas da API e gerenciar as requisições HTTP.
* **SQLite:** Banco de dados local simples e prático, ideal para projetos pequenos e de estudo.

## Primeiros passos 

Siga essas instruções para configurar a executar o projeto em sua máquina local.

## Clonando o Repositório

```bash
git clone https://github.com/MaCristy/sistema_habilitacao.git
cd sistema_habilitacao
```

## 🗂️ Estrutura do Projeto

```bash
.
│── app.py               # Arquivo principal que inicia a API
│── services.py          # Funções de lógica e regras de negócio
│── model.py             # Definição dos modelos e estrutura do banco
│── cnhs.db              # Banco SQLite (não recomendado versionar)
│── requirements.txt     # Dependências do projeto
└── README.md            # Documentação
```

## 🚀 Como rodar 

Siga os passos abaixos para configurar e executar o `Sistema de Habilitação` em sua maquina.

### Pré-requisitos

Certifique-se de ter o seguinte instalado antes de iniciar:

**Python 3.10+:** Necessário para executar a aplicação Flask.
**Pip:** Instalador de pacotes do Python.

### 1. Configuração do Ambiente

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/MaCristy/sistema_habilitacao.git
   cd sistema_habilitacao
   ```

2. **Crie e Ative o Ambiente Virtual**
   ```bash
   python -m venv venv
   # No Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # No Windows (CMD):
   .venv\Scripts\activate.bat
   # No macOS / Linux:
   source .venv/bin/activate
   ```

3. **Instale as Dependências**
   Se você estiver usando o requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
   Caso ainda não o tenha gerado:
   ```bash
   pip install Flask
   ```

### 2. Executando o servidor

   Com o ambiente virtual ativo, execute:
   ```bash
   python app.py
   ```
   Se tudo estiver correto, você verá o servidor Flask iniciar, e a API estará acessível em:
   ```bash
   http://localhost:5000
   ```

## 💻 Testando no Postman

1. Ler/Buscar dados
* **Endpoint:** `GET /habilitacoes`
* **Descrição:** Listar todas as habilitações


2. Enviar/Criar dados
* **Endpoint:** `POST /habilitacoes`
* **Descrição:** Criar nova habilitação
* **Corpo da Requisição(JSON):**
  
  ```JSON
  {
  "nome": "Cristina",
  "cpf": "000.000.000-00",
  "categoria": "B"
  }
  ```


3. Atualizar dados
* **Endpoint:** `PUT /habilitacoes/1`
* **Descrição:** Atualizar habilitação
* **Corpo da Requisição(JSON):**
  
  ```JSON
  {
  "nome": "Cristina",
  "cpf": "111.222.333-44",
  "categoria": "A"
  }
  ```

4. Deletar dados
* **Endpoint:** `DELETE /habilitacoes/1`
* **Descrição:** Excluir habilitação
* **Corpo da Requisição(JSON):**
  
