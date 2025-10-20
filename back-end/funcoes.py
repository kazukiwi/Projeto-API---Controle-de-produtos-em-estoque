from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:  
        try:
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        categoria VARCHAR(50),
        preco DECIMAL(10,2),
        quantidade INT
        );
        """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()
criar_tabela()

def adicionar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
            INSERT INTO produtos (nome, categoria, preco, quantidade)
            VALUES (%s, %s, %s, %s)
            """, (nome, categoria, preco, quantidade))
            conexao.commit()
        except Exception as error:
            print(f"Erro: {error}")
        finally:
            cursor.close()
            conexao.close()

def listar_produtos():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
            SELECT * FROM produtos ORDER BY id
             """)
            return cursor.fetchall()
        except Exception as error:
            print(f"Erro: {error}")
        finally:
            cursor.close()
            conexao.close()

def atualizar_produtos(preco_novo, quantidade_novo, id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
            UPDATE produtos SET preco = %s, quantidade = %s
            WHERE id = %s
            """,  (preco_novo, quantidade_novo, id_produto))
            conexao.commit()
        except Exception as error:
            print(f"Erro: {error}")
        finally:
            cursor.close()
            conexao.close()

def deletar_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""
            DELETE FROM produtos 
            WHERE id = %s
            """, (id_produto,))
            conexao.commit()
        except Exception as error:
            print(f"Erro: {error}")
        finally:
            cursor.close()
            conexao.close()

def buscar_produto(id_produto):
    conexao, cursor = conectar()
    if conexao:  
        try:
            cursor.execute("""
        SELECT * FROM produtos WHERE id = %s
        """, (id_produto,))
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao buscar o filme: {erro}")
            return {}
        finally:
            cursor.close()
            conexao.close()