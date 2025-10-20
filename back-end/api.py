from fastapi import FastAPI
from funcoes import adicionar_produto, listar_produtos, atualizar_produtos, deletar_produto

app = FastAPI(title="Controle de produtos em estoque")

@app.get("/")
def home():
    return {
        "mensagem": "Bem-vindo ao Controle de produtos!"
    }

@app.get("/produtos/listar")
def listar():
    produtos = listar_produtos()
    lista = []
    for produto in produtos:
        lista.append({
            "id": produto[0],
            "nome": produto[1],
            "categoria": produto[2],
            "preco": produto[3],
            "quantidade": produto[4]
        })
    return {
        "produtos": lista
    }

@app.post("/produtos/criar")
def adicionar(nome: str, categoria: str, preco: float, quantidade: int):
    adicionar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Filme adicionado com sucesso!"}