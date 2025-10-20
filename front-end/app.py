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
        produtos = response.json().get("produtos", [])
        if produtos:
            for produto in produtos:
                st.write(f"**🍴{produto['nome']}** ({produto['categoria']})  \n 💵R${produto['preco']}  \n 🛒 Quantidade: {produto['quantidade']}")
        else:
            st.error("Produtos não encontrados!")
    else:
        st.error("Erro ao conectar na api")

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
            st.success("Filme adicionado com sucesso")
        else:
            st.error("Erro ao adicionar filme")