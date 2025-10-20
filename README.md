# 📦 Projeto API - Controle de Produtos em Estoque
Uma aplicação Full Stack projetada para oferecer uma solução robusta e eficiente para o controle e gestão de inventário de produtos. O sistema é dividido em um back-end (API) responsável pela lógica de negócio e persistência de dados, e um front-end (interface do usuário) para interação.

## ✨ Visão Geral
O objetivo principal deste projeto é centralizar e automatizar o controle de estoque. Ele permite que usuários realizem operações essenciais para manter o inventário preciso e atualizado, garantindo visibilidade sobre a quantidade de itens disponíveis.

## 🛠️ Funcionalidades Principais (API)
O back-end expõe endpoints RESTful para gerenciar o catálogo de produtos e as operações de estoque:

CRUD de Produtos:

- POST /produtos: Cadastrar um novo produto.
- GET /produtos: Listar todos os produtos ou buscar por ID/nome.
- PUT /produtos/{id}: Atualizar informações de um produto existente.
- DELETE /produtos/{id}: Remover um produto do catálogo.

Controle de Estoque:

- GET /estoque/{id}: Consultar o nível de estoque de um produto específico.

- POST /estoque/entrada: Registrar a entrada de um lote de produtos.

- POST /estoque/saida: Registrar a saída/venda de produtos.

## 🚀 Tecnologias Utilizadas
A solução é composta por duas partes distintas:
| Componente | Tecnologia Princiapal | 
| :------- | :------: |
| Back-End     | Python   | 
| Front-End   | Streamlit   |
| Banco de dados      | PostgreSQL      |

## ⚙️ Instalação e Configuração
Siga os passos abaixo para configurar e executar o projeto localmente.

1. ###  Back-end (API em Python)

    1. #### Clone o repositório:
        ```
        git clone https://github.com/kazukiwi/Projeto-API---Controle-de-produtos-em-estoque.git

        cd 
        Projeto-API---Controle-de-produtos-em-estoque
        ```

    2. #### Crie um ambiente virtual (recomendado):
        ```
        python3 -m venv venv

            source venv/bin/activate  - No Linux/macOS

            .\venv\Scripts\activate - No Windows (PowerShell)```

    3. #### Instale as dependências do Python: 
        As dependências estão listadas no arquivo requirements.txt na raiz do projeto.

        ```pip install -r ../requirements.txt```

    4. #### Configuração de Variáveis de Ambiente: 
    
        Crie um arquivo .env no diretório back-end e defina as variáveis de ambiente necessárias (como credenciais do banco de dados, porta, etc.).

2. ### Front-end

    1. #### Navegue até o diretório do front-end:

        ```cd ../front-end```

    2. #### Inicie a aplicação Streamlit

        ```streamlit run app_estoque.py```

3. ### API

    1. #### Navegue até o diretório do back-end

        ```cd back-end```

    2. #### Execute o servidor da API:

        ```python -m uvicorn api:app --reload```

