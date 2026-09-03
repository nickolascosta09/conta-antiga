from db_manager import get_connection

def inserir_produto(nome, preco, unidade):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO produto (nome, preco, unidade) VALUES (?,?,?)""", (nome, preco, unidade))
        conn.commit()
        produto_id = cursor.lastrowid
        conn.close()
        return True, produto_id
    except Exception as e:
        return False, str(e)
    
def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produto ORDER BY nome")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def buscar_produtos(nome):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produto WHERE nome LIKE ? ORDER BY nome", (f'%{nome}%',))
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def preencher_produtos(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produto WHERE id = ?", (id,))
    produto = cursor.fetchone()
    conn.close()
    return produto

def atualizar_produto(produto_id, nome, preco, unidade):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""UPDATE produto SET nome=?, preco=?, unidade=? WHERE id=?""",(nome, preco, unidade, produto_id))
        conn.commit()
        conn.close()
        return True, "Produto atualizado com sucesso!"
    except Exception as e:
        return False, str(e)
    
def excluir_produto(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produto WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return True, "Produto excluído com sucesso!"
    except Exception as e:
        return False, str(e)