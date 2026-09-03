import db_manager

def inserir_nota_fatura(dados_nf, itens):
    try:
        conn = db_manager.get_connection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO nota_fatura (numero_nf, contrato, cliente_id, data_emissao, vencimento, valor_locacao, valor_total_nota, valor_extenso, observacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (dados_nf['numero_nf'], dados_nf['contrato'], dados_nf['cliente_id'], dados_nf['data_emissao'], dados_nf['vencimento'], dados_nf['valor_locacao'], dados_nf['valor_total_nota'], dados_nf['valor_por_extenso'], dados_nf['observacoes']
        ))
        nf_id = cursor.lastrowid
        for i in itens:
            cursor.execute("""INSERT INTO item_nota_fatura (nf_id, codigo_produto, descricao, unidade, quantidade, valor_unitario, valor_total) VALUES (?, ?, ?, ?, ?, ?, ?)""", (nf_id, i['codigo_produto'], i['descricao'], i['unidade'], i['quantidade'], i['valor_unitario'], i['valor_total']))
        conn.commit()
        conn.close()
        return True, nf_id
    except Exception as e:
        return False, str(e)
    
def buscar_nota_fatura(nf_id):
    try:
        conn = db_manager.get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT nf.id, nf.numero_nf, nf.contrato, nf.cliente_id, nf.data_emissao, nf.vencimento, nf.valor_locacao, nf.valor_total_nota, nf.valor_extenso, nf.observacao, c.nome, c.cpf_cnpj, c.telefone, c.cep, c.endereco, c.numero, c.complemento, c.bairro, c.cidade, c.uf FROM nota_fatura nf JOIN cliente c ON c.id = nf.cliente_id WHERE nf.id = ?""", (nf_id,))
        nota = cursor.fetchone()
        if not nota:
            return None
        nf_data = {
            'id': nota[0],
            'numero_nf': nota[1],
            'contrato': nota[2],
            'cliente_id': nota[3],
            'data_emissao': nota[4],
            'vencimento': nota[5],
            'valor_locacao': nota[6],
            'valor_total_nota': nota[7],
            'valor_por_extenso': nota[8],
            'observacoes': nota[9],
            'cliente_nome': nota[10],
            'cliente_cpf_cnpj': nota[11],
            'cliente_telefone': nota[12],
            'cliente_cep': nota[13],
            'cliente_rua': nota[14],
            'cliente_numero': str(nota[15]),
            'cliente_complemento': nota[16],
            'cliente_bairro': nota[17],
            'cliente_cidade': nota[18],
            'cliente_uf': nota[19],
        }
        cursor.execute("""SELECT codigo_produto, descricao, unidade, quantidade, valor_unitario, valor_total FROM item_nota_fatura WHERE nf_id = ?""", (nf_id,))
        itens = cursor.fetchall()
        nf_data['itens'] = [
            {
                'codigo_produto': str(i[0]),
                'descricao': i[1],
                'unidade': i[2],
                'quantidade': float(i[3]),
                'valor_unitario': float(i[4]),
                'valor_total': float(i[5]),
            }
            for i in itens
        ]
        conn.close()
        return nf_data
    except Exception as e:
        print(f"Erro ao buscar nota fatura: {e}")
        return None
