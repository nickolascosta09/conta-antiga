import sqlite3
from db_manager import get_connection

def inserir_cliente(nome, email, cpf_cnpj, telefone, cep, endereco, numero, complemento, bairro, cidade, uf):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO cliente (nome, email, cpf_cnpj, telefone, cep, endereco, numero, complemento, bairro, cidade, uf) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (nome, email, cpf_cnpj, telefone, cep, endereco, numero, complemento, bairro, cidade, uf))
        conn.commit()
        cliente_id = cursor.lastrowid
        conn.close()
        return True, cliente_id
    except sqlite3.IntegrityError:
        return False, "CPF/CNPJ já cadastrado"
    except Exception as e:
        return False, str(e)

def listar_clientes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente ORDER BY nome")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def buscar_cliente(nome):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente WHERE nome LIKE ? ORDER BY nome", (f'%{nome}%',))
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def preenche_cliente(cliente_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cliente WHERE id = ?", (cliente_id,))
    cliente = cursor.fetchone()
    conn.close()
    return cliente

def atualizar_cliente(id, nome, email, cpf_cnpj, telefone, cep, endereco, numero, complemento, bairro, cidade, uf):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""UPDATE cliente SET nome=?, email=?, cpf_cnpj=?, telefone=?, cep=?, endereco=?, numero=?, complemento=?, bairro=?, cidade=?, uf=? WHERE id=?""", (nome, email, cpf_cnpj, telefone, cep, endereco, numero, complemento, bairro, cidade, uf, id))
        conn.commit()
        conn.close()
        return True, "Cliente atualizado com sucesso"
    except sqlite3.IntegrityError:
        return False, "CPF/CNPJ já cadastrado"
    except Exception as e:
        return False, str(e)
    
def excluir_cliente(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cliente WHERE id=?", (id,))
        conn.commit()
        conn.close()
        return True, "Cliente excluído com sucesso"
    except Exception as e:
        return False, str(e)