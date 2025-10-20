import streamlit as st
import requests

st.set_page_config(page_title="Controle de produtos Harity", page_icon="🐱‍💻")

st.title("Controle de produtos 🛒")

API_URL = "http://127.0.0.1:8000"

menu = st.sidebar.radio("Menu", ["Listar", "Criar", "Atualizar", "Deletar"])

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