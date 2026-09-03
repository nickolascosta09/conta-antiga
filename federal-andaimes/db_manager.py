import sqlite3
import os
from sqlite3 import Connection

DATABASE_NAME = 'federal.db'

def initialize_database():
    new_db = not os.path.exists(DATABASE_NAME)
    if new_db:
        print('Criando novo banco de dados')
    else:
        print('Banco de dados encontrado, conectando...')
    with get_connection() as conn:
        create_tables(conn)
        if new_db:
            print('Banco de dados criado com sucesso!')
        else:
            print('Banco de dados conectado com sucesso!')

def get_connection() -> Connection:
    return sqlite3.connect(DATABASE_NAME)

def create_tables(conn: Connection):
    create_cliente_table = """CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT, cpf_cnpj VARCHAR(14) NOT NULL UNIQUE, telefone TEXT, cep TEXT, endereco TEXT, numero INTEGER, complemento TEXT, bairro TEXT, cidade TEXT, uf VARCHAR(2), data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP)"""
    create_produto_table = """CREATE TABLE IF NOT EXISTS produto (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, preco DECIMAL(10,2) NOT NULL, unidade VARCHAR(3), data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP)"""
    create_nf_table = """CREATE TABLE IF NOT EXISTS nota_fatura (id INTEGER PRIMARY KEY AUTOINCREMENT, numero_nf INTEGER NOT NULL, contrato TEXT, cliente_id INTEGER NOT NULL, data_emissao DATETIME DEFAULT CURRENT_TIMESTAMP, vencimento TEXT NOT NULL, valor_locacao DECIMAL(10,2) NOT NULL, valor_total_nota DECIMAL(10,2), valor_extenso TEXT, observacao TEXT, data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (cliente_id) REFERENCES cliente (id))"""
    create_item_nf_table = """CREATE TABLE IF NOT EXISTS item_nota_fatura (id INTEGER PRIMARY KEY AUTOINCREMENT, nf_id INTEGER NOT NULL, codigo_produto INTEGER, descricao TEXT, unidade VARCHAR(3), quantidade INTEGER, valor_unitario DECIMAL(10,2), valor_total DECIMAL(10,2), FOREIGN KEY (nf_id) REFERENCES nota_fatura (id))"""
    cursor = conn.cursor()
    cursor.execute(create_cliente_table)
    cursor.execute(create_produto_table)
    cursor.execute(create_nf_table)
    cursor.execute(create_item_nf_table)
    conn.commit()
    print('Tabelas criadas/verificadas com sucesso!')

def test_connection() -> bool:
    try:
        with get_connection() as conn:
            return conn is not None
    except sqlite3.Error as e:
        print(f'Erro ao testar conexão: {e}')
        return False
    
def get_database_info() -> str:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT sqlite_version()')
            version = cursor.fetchone()[0]
            return f'SQLITE {version} - Arquivo: {os.path.abspath(DATABASE_NAME)}'
    except sqlite3.Error as e:
        return f'Erro ao obter informações do banco: {e}'