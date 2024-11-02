# EFEIROOM

## Tecnologias e Ferramentas Utilizadas

### Linguagens de Programação

| Linguagem     | Descrição                                                    |
|---------------|------------------------------------------------------------|
| Python        | Usada pela sua facilidade de compreensão e flexibilidade.  |
| JavaScript    | Utilizada para interatividade no frontend e comunicação no backend. |

### Frameworks

| Framework     | Descrição                                                    |
|---------------|------------------------------------------------------------|
| Django        | Utilizado para o desenvolvimento da aplicação web, facilitando a criação de estruturas de banco de dados e gerenciamento de backend. |
| React         | Utilizado para criar interfaces de usuário dinâmicas e interativas. |
| Node.js       | Utilizado para gerenciar o backend e facilitar a comunicação em tempo real via WebRTC. |

### Padrões de Design

| Padrão        | Descrição                                                    |
|---------------|------------------------------------------------------------|
| MVT           | Estrutura do Django que organiza o código em modelos (dados), templates (visualização) e views (lógica de negócios). |
| Programação Orientada a Objetos | Utilizada no Django para modelar classes e entidades que se traduzem em tabelas de banco de dados. |
| Conexão Peer-to-Peer | Implementada via WebRTC para comunicação direta entre clientes, descentralizando funções de rede. |

## Instruções de Execução

### Pré-requisitos

- Python 3.x
- Node.js
- npm (gerenciador de pacotes do Node.js)

### Configuração do Django

1. **Instalar Dependências**

   Navegue até o diretório do seu projeto Django e execute:

   ```bash
   pip install -r requirements.txt


2. **Migrar o Banco de Dados** 

    Após instalar as dependências, aplique as migrações do banco de dados:

   ```bash
      python manage.py migrate


3. **Rodar o Servidor**
Para iniciar o servidor de desenvolvimento do Django, execute o seguinte comando:

    ```bash
    python manage.py runserver

O servidor estará disponível em http://127.0.0.1:8000/.

###Configuração do Node.js para WebRTC

4. **Instalar Dependências**
Navegue até o diretório do seu projeto Node.js e instale as dependências necessárias:
 
   ```bash
      npm install

5. **Rodar o Servidor**
Inicie o servidor Node.js com o seguinte comando:

   ```bash
      node server.js

O servidor estará disponível na porta especificada no seu arquivo de configuração (por padrão, geralmente é http://localhost:3000/).

