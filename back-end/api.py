from fastapi import FastAPI
from funcoes import adicionar_produto, listar_produtos, atualizar_produtos, deletar_produto

app = FastAPI(title="Controle de produtos em estoque")

@app.get("/")
def home():
    return {
        "mensagem": "Bem-vindo ao Controle de produtos!"
    }