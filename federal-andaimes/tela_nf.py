import tkinter as tk
import os as sistema_os
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
from pathlib import Path
from datetime import datetime, timedelta
try:
    import db_nf
    import db_cliente
    import db_produto
    import util
    import pdf_generator
except ImportError as e:
    print(f'Erro ao importar módulos: {e}')

janela = None
campos = {}
valor_unitario_atual = 0.0
tree_itens = None
itens_lista = []
nf_selecionada = None
cliente_selecionado = None

def abrir_tela_nf():
    global janela, campos, tree_itens
    janela = tk.Toplevel()
    janela.title("Nota Fatura - Locação de Bens Móveis")
    janela.geometry("1400x850")
    try:
        pasta_sistema = sistema_os.path.join(sistema_os.path.expanduser("~/Documents"), "Federal Andaimes - Sistema")
        caminho_icone = sistema_os.path.join(pasta_sistema, "icon.ico")
        if not sistema_os.path.exists(caminho_icone):
            caminho_icone = sistema_os.path.join(sistema_os.path.dirname(__file__), "icon.ico")
        if sistema_os.path.exists(caminho_icone):
            janela.iconbitmap(caminho_icone)
    except:
        pass
    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (1400 // 2)
    y = (janela.winfo_screenheight() // 2) - (850 // 2)
    janela.geometry(f"1400x850+{x}+{y}")
    canvas = tk.Canvas(janela)
    scrollbar = tk.Scrollbar(janela, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    criar_secao_cabecalho(scrollable_frame)
    criar_secao_cliente(scrollable_frame)
    criar_secao_fatura(scrollable_frame)
    criar_secao_itens(scrollable_frame)
    criar_secao_totais(scrollable_frame)
    criar_secao_observacoes(scrollable_frame)
    criar_secao_botoes(janela)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    nova_nf()

def criar_secao_cabecalho(parent):
    global campos
    frame = tk.LabelFrame(parent, text="FEDERAL ANDAIMES", padx=10, pady=10)
    frame.pack(fill='x', padx=10, pady=5)
    info_frame = tk.Frame(frame)
    info_frame.pack(side='left', fill='both', expand=True)
    tk.Label(info_frame, text="Nome Empresarial: 60.067.070 - Sonia Maria Leobons da Silva", font=("Arial", 9)).pack(anchor='w')
    tk.Label(info_frame, text="Endereço: Avenida Tomas Alves de Figuereido, 150, C2", font=("Arial", 9)).pack(anchor='w')
    tk.Label(info_frame, text="Vila Hepacaré - Lorena - SP - CEP 12608-356", font=("Arial", 9)).pack(anchor='w')
    tk.Label(info_frame, text="Cel.: (12) 99776-4144", font=("Arial", 9)).pack(anchor='w')
    tk.Label(info_frame, text="CNPJ: 60.067.070/0001-99", font=("Arial", 9)).pack(anchor='w')
    nf_frame = tk.Frame(frame)
    nf_frame.pack(side='right')
    tk.Label(nf_frame, text=" Nº:", font=("Arial", 10, "bold")).pack()
    campos['numero_nf'] = tk.Entry(nf_frame, width=15, font=("Arial", 12, "bold"), justify='center')
    campos['numero_nf'].pack()
    tk.Label(nf_frame, text="Contrato", font=("Arial", 10, "bold")).pack()
    campos['contrato'] = tk.Entry(nf_frame, width=15, font=("Arial", 12, "bold"), justify='center')
    campos['contrato'].pack()
    tk.Label(nf_frame, text="Data Emissão:", font=("Arial", 9)).pack(pady=(10, 0))
    campos['data_emissao'] = tk.Entry(nf_frame, width=12, font=("Arial", 10), justify='center')
    campos['data_emissao'].pack()
    campos['data_emissao'].config(state='readonly')

def criar_secao_cliente(parent):
    global campos
    frame = tk.LabelFrame(parent, text="DESTINATÁRIO", padx=10, pady=10)
    frame.pack(fill='x', padx=10, pady=5)
    tk.Label(frame, text="CLIENTE:*", font=("Arial", 10)).pack(side='left', padx=5)
    campos['cliente_var'] = tk.StringVar()
    campos['cliente_combo'] = ttk.Combobox(frame, textvariable=campos['cliente_var'], width=50, font=("Arial", 10), state='readonly')
    campos['cliente_combo'].pack(side='left', padx=5)
    campos['cliente_combo'].bind('<<ComboboxSelected>>', selecionar_cliente)
    carregar_clientes()

def criar_secao_fatura(parent):
    global campos
    frame = tk.LabelFrame(parent, text="FATURA", padx=10, pady=10)
    frame.pack(fill='x', padx=10, pady=5)
    tk.Label(frame, text="VENCIMENTO (dias):*", font=("Arial", 10)).pack(side='left', padx=5)
    campos['vencimento'] = tk.Entry(frame, width=8, font=("Arial", 10))
    campos['vencimento'].pack(side='left', padx=5)
    campos['vencimento'].insert(0, '30')
    campos['vencimento'].bind('<KeyRelease>', calcular_data_vencimento)
    tk.Label(frame, text="DATA VENCIMENTO:", font=("Arial", 10)).pack(side='left', padx=(20, 5))
    campos['data_vencimento'] = tk.Entry(frame, width=12, font=("Arial", 10), state='readonly')
    campos['data_vencimento'].pack(side='left', padx=5)
    tk.Label(frame, text="VALOR:", font=("Arial", 10)).pack(side='left', padx=(20, 5))
    campos['valor_locacao'] = tk.Entry(frame, width=15, font=("Arial", 10))
    campos['valor_locacao'].pack(side='left', padx=5)
    campos['valor_locacao'].insert(0, 'R$ 0,00')
    campos['valor_locacao'].bind('<KeyRelease>', aplicar_mascara_valor_locacao)
    campos['valor_locacao'].bind('<FocusIn>', focar_campo_valor_locacao)
    campos['valor_locacao'].bind('<FocusOut>', lambda e: calcular_totais())
    tk.Label(frame, text="VALOR POR EXTENSO:", font=("Arial", 10)).pack(side='left', padx=(20, 5))
    campos['valor_extenso'] = tk.Entry(frame, width=40, font=("Arial", 10))
    campos['valor_extenso'].pack(side='left', padx=5)
    
def criar_secao_itens(parent):
    global campos, tree_itens
    frame = tk.LabelFrame(parent, text="DADOS DO PRODUTO", padx=10, pady=10)
    frame.pack(fill='both', expand=True, padx=10, pady=5)
    add_frame = tk.Frame(frame)
    add_frame.pack(fill='x', pady=5)
    tk.Label(add_frame, text="Produto:", font=("Arial", 9)).pack(side='left', padx=2)
    campos['produto_var'] = tk.StringVar()
    campos['produto_combo'] = ttk.Combobox(add_frame, textvariable=campos['produto_var'], width=30, font=("Arial", 9), state='readonly')
    campos['produto_combo'].pack(side='left', padx=2)
    campos['produto_combo'].bind('<<ComboboxSelected>>', selecionar_produto)
    tk.Label(add_frame, text="Qtd:", font=("Arial", 9)).pack(side='left', padx=2)
    campos['quantidade'] = tk.Entry(add_frame, width=8, font=("Arial", 9))
    campos['quantidade'].pack(side='left', padx=2)
    campos['quantidade'].insert(0, '1')
    btn_adicionar = tk.Button(add_frame, text="Adicionar Item", command=adicionar_item, font=("Arial", 9), bg='#228B22', fg='white', cursor='hand2')
    btn_adicionar.pack(side='left', padx=5)
    btn_remover = tk.Button(add_frame, text="Remover Item", command=remover_item, font=("Arial", 9), bg='#DC143C', fg='white', cursor='hand2')
    btn_remover.pack(side='left', padx=2)
    tree_frame = tk.Frame(frame)
    tree_frame.pack(fill='both', expand=True, pady=5)
    scrollbar = ttk.Scrollbar(tree_frame)
    scrollbar.pack(side='right', fill='y')
    tree_itens = ttk.Treeview(tree_frame, columns=('Código', 'Descrição', 'Unid', 'Qtd', 'Valor Unitario', 'Valor Total'), show='headings', height=8, yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree_itens.yview)
    tree_itens.heading('Código', text='CÓD')
    tree_itens.heading('Descrição', text='DESCRIÇÃO')
    tree_itens.heading('Unid', text='UNID')
    tree_itens.heading('Qtd', text='QUANT')
    tree_itens.heading('Valor Unitario', text='VALOR UNITÁRIO')
    tree_itens.heading('Valor Total', text='VALOR TOTAL')
    tree_itens.column('Código', width=80, anchor='center')
    tree_itens.column('Descrição', width=400, anchor='w')
    tree_itens.column('Unid', width=60, anchor='center')
    tree_itens.column('Qtd', width=80, anchor='center')
    tree_itens.column('Valor Unitario', width=120, anchor='e')
    tree_itens.column('Valor Total', width=120, anchor='e')
    tree_itens.pack(side='left', fill='both', expand=True)
    carregar_produtos()

def criar_secao_totais(parent):
    global campos
    frame = tk.LabelFrame(parent, text="TOTAIS", padx=10, pady=10)
    frame.pack(fill='x', padx=10, pady=5)
    totais_frame = tk.Frame(frame)
    totais_frame.pack(side='right')
    tk.Label(totais_frame, text="VALOR DA LOCAÇÃO:", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, sticky='e')
    campos['valor_locacao_display'] = tk.Entry(totais_frame, width=15, font=("Arial", 12, "bold"),justify='right', state='readonly', fg='#006400')
    campos['valor_locacao_display'].grid(row=1, column=1, padx=5)
    tk.Label(totais_frame, text="VALOR TOTAL DA NOTA:", font=("Arial", 10, "bold")).grid(row=1, column=2, padx=5, sticky='e')
    campos['valor_total'] = tk.Entry(totais_frame, width=15, font=("Arial", 12, "bold"),justify='right', state='readonly', fg='#006400')
    campos['valor_total'].grid(row=1, column=3, padx=5)

def criar_secao_observacoes(parent):
    global campos
    frame = tk.LabelFrame(parent, text="DADOS ADICIONAIS", padx=10, pady=10)
    frame.pack(fill='both', padx=10, pady=5)
    tk.Label(frame, text="OBSERVAÇÕES:", font=("Arial", 10)).pack(anchor='w')
    campos['observacoes'] = scrolledtext.ScrolledText(frame, width=80, height=4, font=("Arial", 9), wrap=tk.WORD)
    campos['observacoes'].pack(fill='both', expand=True, pady=5)

def criar_secao_botoes(parent):
    frame = tk.Frame(parent, bg='#F0F0F0')
    frame.pack(side='bottom', fill='x', pady=10)
    # btn_nova = tk.Button(frame, text="Nova NF", command=nova_nf, width=12, height=1, font=("Arial", 10), bg='#4682B4', fg='white', cursor='hand2')
    # btn_nova.pack(side='left', padx=5)
    btn_salvar = tk.Button(frame, text="Salvar", command=salvar_nf, width=12, height=1, font=("Arial", 10), bg='#228B22', fg='white', cursor='hand2')
    btn_salvar.pack(side='left', padx=5)
    btn_imprimir = tk.Button(frame, text="Imprimir PDF", command=imprimir_pdf, width=12, height=1, font=("Arial", 10), bg='#4682b4', fg='white', cursor='hand2')
    btn_imprimir.pack(side='left', padx=5)
    btn_sair = tk.Button(frame, text="Sair", command=sair, width=12, height=1, font=("Arial", 10), bg="#b61b1b", fg='white', cursor='hand2')
    btn_sair.pack(side='left', padx=5)

def carregar_clientes():
    clientes = db_cliente.listar_clientes()
    valores = [f"{c[0]} - {c[1]}" for c in clientes]
    campos['cliente_combo']['values'] = valores

def carregar_produtos():
    produtos = db_produto.listar_produtos()
    valores = [f"{p[0]} - {p[1]}" for p in produtos]
    campos['produto_combo']['values'] = valores

def selecionar_cliente(event):
    global cliente_selecionado
    valor = campos['cliente_var'].get()
    if valor and isinstance(valor, str):
        cliente_id = int(valor.split(' - ')[0])
        cliente_selecionado = db_cliente.preenche_cliente(cliente_id)

def selecionar_produto(event):
    global valor_unitario_atual
    valor = campos['produto_var'].get()
    if valor:
        produto_id = int(valor.split(' - ')[0])
        produto = db_produto.preencher_produtos(produto_id)
        if produto:
            preco = float(produto[2]) if produto[2] is not None else 0.0
            valor_unitario_atual = preco
    # valor = campos['produto_var'].get()
    # if valor:
    #     produto_id = int(valor.split(' - ')[0])
    #     produto = db_produto.preencher_produtos(produto_id)
    #     if produto:
    #         preco = float(produto[2]) if produto[2] is not None else 0.0
    #         campos['valor_unitario'].delete(0, tk.END)
    #         campos['valor_unitario'].insert(0, util.formatar_moeda(preco))

def abrir_cadastro_cliente():
    try:
        import tela_clientes
        tela_clientes.abrir_tela_clientes()
        janela.after(1000, carregar_clientes)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao abrir cadastro: {e}")

def adicionar_item():
    global itens_lista
    global valor_unitario_atual
    produto_selecionado = campos['produto_var'].get()
    if not produto_selecionado:
        messagebox.showwarning("Aviso", "Selecione um produto!")
        return
    try:
        produto_id = int(produto_selecionado.split(' - ')[0])
        produto_nome = produto_selecionado.split(' - ')[1]
        quantidade = float(campos['quantidade'].get())
        # valor_unitario = util.converter_float(campos['valor_unitario'].get())
        valor_unitario = float(valor_unitario_atual or 0.0)
        if quantidade <= 0:
            messagebox.showwarning("Aviso", "Quantidade deve ser maior que zero!")
            return
        valor_total = quantidade * valor_unitario
        item = {
            'codigo_produto': str(produto_id),
            'descricao': produto_nome,
            'unidade': 'UN',
            'quantidade': quantidade,
            'valor_unitario': valor_unitario,
            'valor_total': valor_total
        }
        itens_lista.append(item)
        tree_itens.insert('', 'end', values=(
            item['codigo_produto'],
            item['descricao'],
            item['unidade'],
            f"{item['quantidade']:.2f}",
            util.formatar_moeda(item['valor_unitario']),
            util.formatar_moeda(item['valor_total'])
        ))
        campos['produto_combo'].set('')
        campos['quantidade'].delete(0, tk.END)
        campos['quantidade'].insert(0, '1')
        # campos['valor_unitario'].delete(0, tk.END)
        # campos['valor_unitario'].insert(0, 'R$ 0,00')
        valor_unitario_atual = 0.0
        calcular_totais()    
    except ValueError:
        messagebox.showerror("Erro", "Valores inválidos! Verifique quantidade e valor.")

def remover_item():
    global itens_lista
    selecionado = tree_itens.selection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um item para remover!")
        return
    index = tree_itens.index(selecionado[0])
    itens_lista.pop(index)
    tree_itens.delete(selecionado[0])
    calcular_totais()

def calcular_totais():
    total_itens = sum(item['valor_total'] for item in itens_lista)
    valor_locacao_texto = campos['valor_locacao'].get()
    valor_locacao = util.converter_float(valor_locacao_texto) if valor_locacao_texto else 0.0
    total_final = total_itens + valor_locacao
    campos['valor_locacao_display'].config(state='normal')
    campos['valor_locacao_display'].delete(0, tk.END)
    campos['valor_locacao_display'].insert(0, util.formatar_moeda(valor_locacao))
    campos['valor_locacao_display'].config(state='readonly')
    campos['valor_total'].config(state='normal')
    campos['valor_total'].delete(0, tk.END)
    campos['valor_total'].insert(0, util.formatar_moeda(total_final))
    campos['valor_total'].config(state='readonly')

def aplicar_mascara_valor(event):
    campo = event.widget
    texto_atual = campo.get()
    if not texto_atual or texto_atual == 'R$ ':
        return
    texto_formatado = util.mascara_moeda(texto_atual)
    if texto_formatado != texto_atual:
        campo.delete(0, tk.END)
        campo.insert(0, texto_formatado)
        campo.icursor(tk.END)

def focar_campo_valor(event):
    campo = event.widget
    texto_atual = campo.get()
    if not texto_atual or texto_atual.strip() == '':
        campo.delete(0, tk.END)
        campo.insert(0, 'R$ 0,00')
        campo.select_range(0, tk.END)

def nova_nf():
    global nf_selecionada, itens_lista, cliente_selecionado
    nf_selecionada = None
    itens_lista = []
    cliente_selecionado = None
    data_atual = datetime.now().strftime("%d/%m/%Y")
    campos['data_emissao'].config(state='normal')
    campos['data_emissao'].delete(0, tk.END)
    campos['data_emissao'].insert(0, data_atual)
    campos['data_emissao'].config(state='readonly')
    campos['contrato'].delete(0, tk.END)
    campos['cliente_combo'].set('')
    campos['vencimento'].delete(0, tk.END)
    campos['valor_extenso'].delete(0, tk.END)
    campos['observacoes'].delete('1.0', tk.END)
    for item in tree_itens.get_children():
        tree_itens.delete(item)
    campos['valor_locacao'].delete(0, tk.END)
    campos['valor_locacao'].insert(0, 'R$ 0,00')
    campos['valor_locacao_display'].config(state='normal')
    campos['valor_locacao_display'].delete(0, tk.END)
    campos['valor_locacao_display'].insert(0, 'R$ 0,00')
    campos['valor_locacao_display'].config(state='readonly')
    campos['valor_total'].config(state='normal')
    campos['valor_total'].delete(0, tk.END)
    campos['valor_total'].insert(0, 'R$ 0,00')
    campos['valor_total'].config(state='readonly')

def salvar_nf():
    global nf_selecionada, cliente_selecionado
    if not cliente_selecionado:
        messagebox.showwarning("Validação", "Selecione um cliente!")
        return
    if not itens_lista:
        messagebox.showwarning("Validação", "Adicione pelo menos um item!")
        return
    total_itens = sum(item['valor_total'] for item in itens_lista)
    # print(total_itens)
    valor_locacao_texto = campos['valor_locacao'].get().strip()
    valor_locacao = util.converter_float(valor_locacao_texto) if valor_locacao_texto else 0.0
    # print(valor_locacao)
    total_final = total_itens + valor_locacao
    # print(total_final)
    vencimento_dias = campos['data_vencimento'].get()
    dados_nf = {
        'numero_nf': campos['numero_nf'].get(),
        'cliente_id': cliente_selecionado[0],
        'data_emissao': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'contrato': campos['contrato'].get(),
        'vencimento': vencimento_dias if vencimento_dias else '01/01/1970', 
        'valor': total_itens, 
        'valor_por_extenso': campos['valor_extenso'].get().strip(),
        'valor_locacao': valor_locacao, 
        'valor_total_nota': total_final, 
        'observacoes': campos['observacoes'].get('1.0', tk.END).strip(),
    }
    if nf_selecionada is None:
        sucesso, resultado = db_nf.inserir_nota_fatura(dados_nf, itens_lista)
        if sucesso:
            nf_selecionada = resultado
            messagebox.showinfo("Sucesso", f"Nota Fatura {dados_nf['numero_nf']} salva com sucesso!")
        else:
            messagebox.showerror("Erro", f"Erro ao salvar NF:\n{resultado}")

def imprimir_pdf():
    global nf_selecionada
    if nf_selecionada is None:
        messagebox.showwarning("Aviso", "Salve a Nota Fatura antes de imprimir!")
        return
    nf = db_nf.buscar_nota_fatura(nf_selecionada)
    if not nf:
        messagebox.showerror("Erro", "Erro ao carregar dados da Nota Fatura!")
        return
    pasta_nf = Path.home() / "Documents" / "Federal Andaimes - Sistema" / "Nota Fatura"
    pasta_nf.mkdir(parents=True, exist_ok=True)
    cliente_nome_limpo = nf['cliente_nome'].strip().replace(' ', '_').replace('/', '-')
    nome_arquivo = f"NF_{cliente_nome_limpo}_{nf['numero_nf']}.pdf"
    caminho_completo = pasta_nf / nome_arquivo
    try:
        sucesso = pdf_generator.gerar_pdf_nota_fatura(nf, str(caminho_completo))
        if sucesso:
            resposta = messagebox.askyesno("PDF gerado com sucesso!",f"Arquivo: {nome_arquivo}\n\n"f"Deseja abrir o arquivo?")
            if resposta:
                sistema_os.startfile(str(caminho_completo))
        else:
            messagebox.showerror("Erro", "Erro ao gerar PDF!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar PDF:\n{str(e)}")

def aplicar_mascara_valor_locacao(event):
    campo = event.widget
    texto_atual = campo.get()
    if not texto_atual or texto_atual == 'R$ ':
        return
    texto_formatado = util.mascara_moeda(texto_atual)
    if texto_formatado != texto_atual:
        campo.delete(0, tk.END)
        campo.insert(0, texto_formatado)
        campo.icursor(tk.END)

def focar_campo_valor_locacao(event):
    campo = event.widget
    texto_atual = campo.get()
    if not texto_atual or texto_atual.strip() == '':
        campo.delete(0, tk.END)
        campo.insert(0, 'R$ 0,00')
        campo.select_range(0, tk.END)

def calcular_data_vencimento(event):
    try:
        dias = int(campos['vencimento'].get())
        data_emissao_str = campos['data_emissao'].get()
        data_emissao = datetime.strptime(data_emissao_str, "%d/%m/%Y")
        data_vencimento = data_emissao + timedelta(days=dias)
        
        campos['data_vencimento'].config(state='normal')
        campos['data_vencimento'].delete(0, tk.END)
        campos['data_vencimento'].insert(0, data_vencimento.strftime("%d/%m/%Y"))
        campos['data_vencimento'].config(state='readonly')
    except:
        campos['data_vencimento'].config(state='normal')
        campos['data_vencimento'].delete(0, tk.END)
        campos['data_vencimento'].config(state='readonly')

def sair():
    resposta = messagebox.askyesno("Confirmar Saída", "Deseja sair da Tela de Nota Fatura?")
    if resposta:
        janela.destroy()