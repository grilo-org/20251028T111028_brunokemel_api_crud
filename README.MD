# API de Usuários - FastAPI

Esta é uma API REST completa desenvolvida com FastAPI, SQLAlchemy e MySQL, que permite gerenciar usuários com operações CRUD completas, autenticação JWT e sistema de segurança robusto.

## 🚀 Tecnologias

- **FastAPI** - Framework web moderno e rápido para Python
- **Uvicorn** - Servidor ASGI para execução da aplicação
- **SQLAlchemy** - ORM para interação com banco de dados
- **Pydantic v2** - Validação e serialização de dados
- **MySQL** - Sistema de gerenciamento de banco de dados relacional
- **JWT** - Autenticação com tokens seguros
- **Bcrypt** - Criptografia de senhas
- **OAuth2** - Sistema de autenticação padrão

## 📁 Estrutura do Projeto

```
📦 api_py/
├── 📁 app/
│   ├── 📁 core/                 # Configurações principais
│   │   ├── 📜 config.py         # Configurações da aplicação e banco
│   │   ├── 📜 security.py       # Autenticação JWT e segurança
│   │   ├── 📜 __init__.py       # Inicialização do módulo core
│   │   └── 📜 example_usage.py  # Exemplos de uso das funcionalidades
│   ├── 📁 routers/              # Rotas da API
│   │   ├── 📜 __init__.py
│   │   └── 📜 users.py          # Rotas de usuários
│   ├── 📜 main.py               # Ponto de entrada da aplicação
│   ├── 📜 models.py             # Modelos do banco de dados (SQLAlchemy)
│   ├── 📜 database.py           # Configuração e conexão com o banco
│   ├── 📜 schemas.py            # Schemas Pydantic para validação
│   └── 📜 crud.py               # Operações CRUD do banco de dados
├── 📁 tests/                    # Testes automatizados
│   └── 📜 test_users.py
├── 📜 requirements.txt          # Dependências do projeto
├── 📜 credenciais.env           # Variáveis de ambiente (não versionado)
├── 📜 .gitignore               # Arquivos ignorados pelo Git
└── 📜 README.md                # Documentação do projeto
```

## 🛠️ Instalação e Execução

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes do Python)
- MySQL Server instalado e configurado

### Passos para instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/brunokemel/api_crud.git
   cd api_crud
   ```

2. **Configure o banco MySQL:**
   - Crie um banco de dados chamado `cadastro_db`
   - Crie o arquivo `credenciais.env` com as seguintes variáveis:
     ```env
     DB_USER=seu_usuario
     DB_PASSWORD=sua_senha
     DB_HOST=localhost
     DB_NAME=cadastro_db
     
     # Configurações JWT
     SECRET_KEY=sua_chave_secreta_muito_segura_aqui
     ALGORITHM=HS256
     ACCESS_TOKEN_EXPIRE_MINUTES=30
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Use Python 3.12.7 ou use vitualização com a versão**(Para compatibilidade com rust https://rustup.rs/ instale localmente se necessario)
````bash
  py -3.12 -m venv venv    
  > .\venv\Scripts\activate
````

5. **Execute a aplicação:**
   ```bash
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   uvicorn app.main:app --reload
   ```

6. **Acesse a documentação interativa:**
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc
   - API Base: http://127.0.0.1:8000

## 📸 Interface da API

<img width="1414" height="636" alt="image" src="https://github.com/user-attachments/assets/c82d26f7-edbf-4455-a294-0cca4c48f1c4" />

**Acesse a documentação interativa:** @http://127.0.0.1:8000/docs

## 📋 Endpoints da API

### Usuários

#### Criar Usuário
- **POST** `/users/`
- **Body:**
  ```json
  {
    "nome": "João Silva",
    "email": "joao@email.com",
    "cpf": "123.456.789-00"
  }
  ```

#### Listar Usuários
- **GET** `/users/`
- **Resposta:** Lista de todos os usuários cadastrados

#### Atualizar Usuário
- **PUT** `/users/{user_id}`
- **Body:**
  ```json
  {
    "nome": "João Silva Atualizado",
    "email": "joao.novo@email.com",
    "cpf": "123.456.789-00"
  }
  ```

#### Deletar Usuário
- **DELETE** `/users/{user_id}`
- **Parâmetros:** `user_id` (ID do usuário a ser deletado)

### Autenticação (Em Desenvolvimento)

#### Login
- **POST** `/token`
- **Body:**
  ```json
  {
    "username": "usuario@email.com",
    "password": "senha123"
  }
  ```

#### Rotas Protegidas
- Todas as rotas de usuários podem ser protegidas com autenticação JWT
- Use o token retornado no login no header: `Authorization: Bearer <token>`

## 🗄️ Modelo de Dados

### User
- `id` (Integer, Primary Key) - Identificador único
- `nome` (String, 100 chars) - Nome do usuário
- `email` (String, 100 chars, Unique) - Email único do usuário
- `cpf` (String, 14 chars, Unique) - CPF único do usuário

## 🔧 Funcionalidades

### ✅ Implementadas
- **CRUD Completo** - Criar, ler, atualizar e deletar usuários
- **Validação de Dados** - Pydantic v2 para validação robusta
- **Banco de Dados MySQL** - Persistência com SQLAlchemy
- **Documentação Automática** - Swagger UI e ReDoc integrados
- **Configurações Centralizadas** - Sistema core modular
- **Segurança JWT** - Autenticação com tokens (infraestrutura pronta)
- **Criptografia de Senhas** - Bcrypt para segurança
- **Pool de Conexões** - Otimização de performance do banco

### 🚧 Em Desenvolvimento
- **Sistema de Login** - Endpoint de autenticação
- **Proteção de Rotas** - Middleware de autenticação
- **Gerenciamento de Sessões** - Refresh tokens

## 🔐 Sistema de Segurança

### Configurações JWT
- **Algoritmo:** HS256
- **Expiração:** 30 minutos (configurável)
- **Chave Secreta:** Definida em `credenciais.env`

### Criptografia
- **Senhas:** Hash bcrypt com salt automático
- **Tokens:** Assinatura digital JWT
- **Conexões:** SSL/TLS para banco de dados

## 📝 Notas Importantes

- ⚠️ **Crie o banco MySQL** `cadastro_db` antes da execução
- 🔑 **Configure o arquivo** `credenciais.env` com suas credenciais
- 🔒 **Mantenha a SECRET_KEY segura** - nunca commite no Git
- 📊 **Validação automática** de dados de entrada e saída
- 📚 **Documentação interativa** disponível em `/docs` e `/redoc`
- 🧪 **Testes automatizados** disponíveis na pasta `tests/`

## 🚀 Próximas Funcionalidades

- [ ] Sistema completo de autenticação
- [ ] Refresh tokens
- [ ] Middleware de autorização
- [ ] Logs estruturados
- [ ] Rate limiting
- [ ] Testes de integração
- [ ] Docker containerization
- [ ] CI/CD pipeline

---

## 📄 Histórico de Versões

### v2.0.0 - Sistema Core Implementado
- ✅ Configuração modular com `app/core/`
- ✅ Sistema de segurança JWT completo
- ✅ CRUD operations otimizadas
- ✅ Pydantic v2 atualizado
- ✅ Estrutura de projeto melhorada

### v1.0.0 - Versão Inicial
- ✅ API básica de usuários
- ✅ Operações CRUD simples
- ✅ Documentação automática