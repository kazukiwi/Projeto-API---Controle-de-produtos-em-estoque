import streamlit as st
import requests

st.set_page_config(page_title="Controle de produtos Harity", page_icon="🐱‍💻")

st.title("Controle de produtos 🛒")

API_URL = "http://127.0.0.1:8000"

menu = st.sidebar.radio("Menu", ["Listar", "Adicionar", "Atualizar", "Deletar"])

if menu == "Listar":
    st.subheader("Todos os produtos disponíveis 🍽")
    response = requests.get(f"{API_URL}/produtos/listar")
    if response.status_code == 200:
        produtos = response.json().get("produtos", {})
        if produtos:
            for produto in produtos:
                st.write(f"**🍴{produto['nome']}** ({produto['categoria']})  \n 💵R${produto['preco']}  \n 🛒 Quantidade: {produto['quantidade']}")
        else:
            st.error("Produtos não encontrados!")
    else:
        st.error("Erro ao conectar na api")

    valor_total_estoque = 0
    for item in produtos:
        valor_total_estoque += item["preco"] * item["quantidade"]
    
    st.subheader("Controle de Estoque")
    st.write(f"Valor total em estoque: R$ {valor_total_estoque:.2f}")

elif menu == "Adicionar":
    st.subheader("Acrescentar um produto")
    nome = st.text_input("Nome do produto")
    categoria = st.text_input("Categoria do produto")
    preco = st.number_input("Preço do produto", min_value=0.01)
    quantidade = st.number_input("Quantidade do produto", min_value=1, step=1)

    if st.button("Cadastrar"):
        params = {
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade
            }
        response = requests.post(f"{API_URL}/produtos/criar", params=params)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso")
        else:
            st.error("Erro ao adicionar o produto")

elif menu == "Atualizar":
    st.subheader("Atualizar um produto")
    id_produto = st.number_input("Coloque o id do produto", min_value=1, step=1)
    preco_novo = st.number_input("Coloque o novo preço")
    nova_quantidade = st.number_input("Coloque a nova quantidade", step=1)

    if st.button("Atualizar"):
        params = {
            "preco_novo": preco_novo,
            "quantidade_novo": nova_quantidade,
        }
        response = requests.put(f"{API_URL}/produtos/atualizar/{id_produto}", params=params)
        if response.status_code == 200:
            params = response.json()
            if "erro" in params:
                st.warning(params["erro"])
            else:
                st.success("Produto atualizado com sucesso")
        else:
            st.error(f"Erro ao atualizar o produto")

elif menu == "Deletar":
    st.subheader("Deletar um produto")
    id_produto = st.number_input("Coloque o id do produto", min_value=1, step=1)

    if st.button("Deletar"):
        response = requests.delete(f"{API_URL}/produtos/deletar/{id_produto}")
        if response.status_code == 200:
            params = response.json()
            if "erro" in params:
                st.warning(params["erro"])
            else:
                st.success("Produto deletado com sucesso")
        else:
            st.error("Erro ao deletar o produto")