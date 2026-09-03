import tkinter as tk
import os
from tkinter import ttk, messagebox
try:
    import db_cliente
    import util
except ImportError as e:
    print(f'Erro ao importar módulos: {e}')

janela = None
tree = None
campos = {}
cliente_selecionado_id = None

def abrir_tela_clientes():
    global janela, tree, campos
    janela = tk.Toplevel()
    janela.title("Gerenciamento de Clientes")
    janela.geometry("1200x750")
    try:
        pasta_sistema = os.path.join(os.path.expanduser("~/Documents"), "Federal Andaimes - Sistema")
        caminho_icone = os.path.join(pasta_sistema, "icon.ico")
        if not os.path.exists(caminho_icone):
            caminho_icone = os.path.join(os.path.dirname(__file__), "icon.ico")
        if os.path.exists(caminho_icone):
            janela.iconbitmap(caminho_icone)
    except:
        pass
    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (1200 // 2)
    y = (janela.winfo_screenheight() // 2) - (750 // 2)
    janela.geometry(f"1200x750+{x}+{y}")
    frame_form = tk.LabelFrame(janela, text="Dados do Cliente", padx=10, pady=10)
    frame_form.pack(fill='x', padx=10, pady=10)
    criar_campos_formulario(frame_form)
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=10)
    criar_botoes(frame_botoes)
    frame_busca = tk.LabelFrame(janela, text="Buscar Cliente", padx=10, pady=10)
    frame_busca.pack(fill='x', padx=10, pady=5)
    criar_area_busca(frame_busca)
    criar_tabela_clientes(janela)
    limpar_campos()

def criar_campos_formulario(frame):
    global campos
    tk.Label(frame, text="Nome:*", font=("Arial", 10)).grid(row=0, column=0, sticky='w', pady=5)
    campos['nome'] = tk.Entry(frame, width=40, font=("Arial", 10))
    campos['nome'].grid(row=0, column=1, padx=5, pady=5, sticky='w')
    tk.Label(frame, text="Email:", font=("Arial", 10)).grid(row=0, column=2, sticky='w', padx=(20, 0), pady=5)
    campos['email'] = tk.Entry(frame, width=30, font=("Arial", 10))
    campos['email'].grid(row=0, column=3, padx=5, pady=5, sticky='w')
    tk.Label(frame, text="CPF/CNPJ:*", font=("Arial", 10)).grid(row=1, column=0, sticky='w', pady=5)
    campos['cpf_cnpj'] = tk.Entry(frame, width=25, font=("Arial", 10))
    campos['cpf_cnpj'].grid(row=1, column=1, padx=5, pady=5, sticky='w')
    campos['cpf_cnpj'].bind('<KeyRelease>', aplicar_mascara_cpf_cnpj)
    tk.Label(frame, text="Telefone:", font=("Arial", 10)).grid(row=1, column=2, sticky='w', padx=(20, 0), pady=5)
    campos['telefone'] = tk.Entry(frame, width=20, font=("Arial", 10))
    campos['telefone'].grid(row=1, column=3, padx=5, pady=5, sticky='w')
    campos['telefone'].bind('<KeyRelease>', aplicar_mascara_telefone)
    tk.Label(frame, text="CEP:", font=("Arial", 10)).grid(row=2, column=0, sticky='w', pady=5)
    campos['cep'] = tk.Entry(frame, width=15, font=("Arial", 10))
    campos['cep'].grid(row=2, column=1, padx=5, pady=5, sticky='w')
    campos['cep'].bind('<KeyRelease>', aplicar_mascara_cep)
    tk.Label(frame, text="Endereço:", font=("Arial", 10)).grid(row=2, column=2, sticky='w', padx=(20, 0), pady=5)
    campos['endereco'] = tk.Entry(frame, width=40, font=("Arial", 10))
    campos['endereco'].grid(row=2, column=3, padx=5, pady=5, sticky='w')
    tk.Label(frame, text="Número:", font=("Arial", 10)).grid(row=3, column=0, sticky='w', pady=5)
    campos['numero'] = tk.Entry(frame, width=10, font=("Arial", 10))
    campos['numero'].grid(row=3, column=1, padx=5, pady=5, sticky='w')
    tk.Label(frame, text="Compl.:", font=("Arial", 10)).grid(row=3, column=2, sticky='w', padx=(20, 0), pady=5)
    campos['complemento'] = tk.Entry(frame, width=30, font=("Arial", 10))
    campos['complemento'].grid(row=3, column=3, padx=5, pady=5, sticky='w')
    tk.Label(frame, text="Bairro:", font=("Arial", 10)).grid(row=4, column=0, sticky='w', pady=5)
    campos['bairro'] = tk.Entry(frame, width=25, font=("Arial", 10))
    campos['bairro'].grid(row=4, column=1, padx=5, pady=5, sticky='w')
    tk.Label(frame, text="Cidade:", font=("Arial", 10)).grid(row=4, column=2, sticky='w', padx=(20, 0), pady=5)
    campos['cidade'] = tk.Entry(frame, width=25, font=("Arial", 10))
    campos['cidade'].grid(row=4, column=3, padx=5, pady=5, sticky='w')
    tk.Label(frame, text="UF:", font=("Arial", 10)).grid(row=4, column=4, sticky='w', padx=(10, 0), pady=5)
    campos['uf'] = tk.Entry(frame, width=5, font=("Arial", 10))
    campos['uf'].grid(row=4, column=5, padx=5, pady=5, sticky='w')

def criar_botoes(frame):
    #btn_novo = tk.Button(frame, text="Novo", command=novo_cliente, width=12, height=1, font=("Arial", 10), bg='#4682B4', fg='white', cursor='hand2')
    #btn_novo.pack(side='left', padx=5)
    btn_salvar = tk.Button(frame, text="Salvar", command=salvar_cliente, width=12, height=1, font=("Arial", 10), bg='#228B22', fg='white', cursor='hand2')
    btn_salvar.pack(side='left', padx=5)
    # btn_editar = tk.Button(frame, text="Editar", command=editar_cliente, width=12, height=1, font=("Arial", 10), bg='#4682B4', fg='white', cursor='hand2')
    # btn_editar.pack(side='left', padx=5)
    btn_excluir = tk.Button(frame, text="Excluir", command=excluir_clientes, width=12, height=1, font=("Arial", 10), bg='#DC143C', fg='white', cursor='hand2')
    btn_excluir.pack(side='left', padx=5)
    btn_sair = tk.Button(frame, text="Sair", command=sair, width=12, height=1, font=("Arial", 10), bg="#E2FA06", fg='black', cursor='hand2')
    btn_sair.pack(side='left', padx=5)
    # btn_limpar = tk.Button(frame, text="Limpar", command=limpar_campos, width=12, height=1, font=("Arial", 10), bg='#A9A9A9', fg='white', cursor='hand2')
    # btn_limpar.pack(side='left', padx=5)

def criar_area_busca(frame):
    tk.Label(frame, text="Nome:", font=("Arial", 10)).pack(side='left', padx=5)
    entry_busca = tk.Entry(frame, width=30, font=("Arial", 10))
    entry_busca.pack(side='left', padx=5)
    def buscar():
        buscar_clientes(entry_busca.get())
    entry_busca.bind('<Return>', lambda e: buscar())
    btn_buscar = tk.Button(frame, text="Buscar", command=buscar, width=12, height=1, font=("Arial", 10), bg='#4682B4', fg='white', cursor='hand2')
    btn_buscar.pack(side='left', padx=5)
    btn_listar = tk.Button(frame, text="Listar Todos", command=listar_todos, width=12, height=1, font=("Arial", 10), bg='#A9A9A9', fg='white', cursor='hand2')
    btn_listar.pack(side='left', padx=5)

def criar_tabela_clientes(parent):
    global tree
    frame_tree = tk.Frame(parent)
    frame_tree.pack(fill='both', expand=True, padx=10, pady=10)
    scrollbar = ttk.Scrollbar(frame_tree)
    scrollbar.pack(side='right', fill='y')
    tree = ttk.Treeview(frame_tree, columns=('ID', 'Nome', 'CPF/CNPJ', 'Telefone'),show='headings', height=15, yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)
    tree.heading('ID', text='ID')
    tree.heading('Nome', text='Nome')
    tree.heading('CPF/CNPJ', text='CPF/CNPJ')
    tree.heading('Telefone', text='Telefone')
    tree.column('ID', width=50, anchor='center')
    tree.column('Nome', width=300, anchor='w')
    tree.column('CPF/CNPJ', width=150, anchor='center')
    tree.column('Telefone', width=150, anchor='center')
    tree.pack(side='left', fill='both', expand=True)
    tree.bind('<<TreeviewSelect>>', selecionar_cliente)

# def novo_cliente():
#     limpar_campos()
#     campos['nome'].focus()

def salvar_cliente():
    global cliente_selecionado_id
    nome = campos['nome'].get().strip()
    cpf_cnpj = campos['cpf_cnpj'].get().strip()
    if not nome:
        messagebox.showwarning("Validação", "Nome é obrigatório!")
        campos['nome'].focus()
        return
    if not cpf_cnpj:
        messagebox.showwarning("Validação", "CPF/CNPJ é obrigatório!")
        campos['cpf_cnpj'].focus()
        return
    cpf_cnpj_limpo = ''.join(filter(str.isdigit, cpf_cnpj))
    if len(cpf_cnpj_limpo) == 11:
        if not util.validar_cpf(cpf_cnpj_limpo):
            messagebox.showwarning("Validação", "CPF inválido!")
            campos['cpf_cnpj'].focus()
            return
    elif len(cpf_cnpj_limpo) == 14:
        if not util.validar_cnpj(cpf_cnpj_limpo):
            messagebox.showwarning("Validação", "CNPJ inválido!")
            campos['cpf_cnpj'].focus()
            return
    else:
        messagebox.showwarning("Validação", "CPF/CNPJ inválido! Digite 11 ou 14 números.")
        campos['cpf_cnpj'].focus()
        return
    email = campos['email'].get().strip()
    telefone = campos['telefone'].get().strip()
    cep = campos['cep'].get().strip()
    endereco = campos['endereco'].get().strip()
    numero = campos['numero'].get().strip()
    complemento = campos['complemento'].get().strip()
    bairro = campos['bairro'].get().strip()
    cidade = campos['cidade'].get().strip()
    uf = campos['uf'].get().strip().upper()
    if cliente_selecionado_id is None:
        sucesso, resultado = db_cliente.inserir_cliente(nome, email, cpf_cnpj_limpo, telefone, cep, endereco, numero, complemento, bairro, cidade, uf)
        if sucesso:
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            limpar_campos()
        else:
            messagebox.showerror("Erro", f"Erro ao cadastrar cliente:\n{resultado}")
    else:
        sucesso, mensagem = db_cliente.atualizar_cliente(cliente_selecionado_id, nome, email, cpf_cnpj_limpo, telefone, cep, endereco, numero, complemento, bairro, cidade, uf)
        if sucesso:
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
            limpar_campos()
            listar_todos()
        else:
            messagebox.showerror("Erro", f"Erro ao atualizar cliente:\n{mensagem}")

# def editar_cliente():
#     if cliente_selecionado_id is None:
#         messagebox.showwarning("Aviso", "Selecione um cliente na tabela para editar.")

def excluir_clientes():
    global cliente_selecionado_id 
    if cliente_selecionado_id is None:
        messagebox.showwarning("Aviso", "Selecione um cliente na tabela para excluir.")
        return
    nome = campos['nome'].get()
    resposta = messagebox.askyesno("Confirmar Exclusão", f"Deseja realmente excluir o cliente '{nome}'?")
    if resposta:
        sucesso, mensagem = db_cliente.excluir_cliente(cliente_selecionado_id)
        if sucesso:
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
            limpar_campos()
            listar_todos()
        else:
            messagebox.showerror("Erro", f"Erro ao excluir cliente:\n{mensagem}")

def buscar_clientes(nome_campo):
    nome = nome_campo.strip()
    if not nome_campo:
        messagebox.showinfo("Busca", "Digite um nome para buscar.")
        return
    for item in tree.get_children():
        tree.delete(item)
    clientes = db_cliente.buscar_cliente(nome)
    if not clientes:
        messagebox.showinfo("Busca", f"Nenhum cliente encontrado com o nome: {nome}")
        return
    for cliente in clientes:
        tree.insert('', 'end', values=(cliente[0], cliente[1], cliente[3], cliente[4], cliente[12]))

def listar_todos():
    for item in tree.get_children():
        tree.delete(item)
    clientes = db_cliente.listar_clientes()
    if not clientes:
        messagebox.showinfo("Informação", "Nenhum cliente cadastrado.")
        return
    for cliente in clientes:
        cpf_cnpj_formatado = util.aplicar_mascara(cliente[3])
        telefone_formatado = util.mascara_telefone(cliente[4]) if cliente[4] else ''
        tree.insert('', 'end', values=(cliente[0], cliente[1], cpf_cnpj_formatado, telefone_formatado, cliente[12]))

def selecionar_cliente(event):
    global cliente_selecionado_id
    selecionado = tree.selection()
    if not selecionado:
        return
    item = tree.item(selecionado[0])
    cliente_id = item['values'][0]
    cliente = db_cliente.preenche_cliente(cliente_id)
    if cliente:
        cliente_selecionado_id = cliente[0]
        campos['nome'].delete(0, tk.END)
        campos['nome'].insert(0, cliente[1] or '')
        campos['email'].delete(0, tk.END)
        campos['email'].insert(0, cliente[2] or '')
        campos['cpf_cnpj'].delete(0, tk.END)
        cpf_cnpj_formatado = util.aplicar_mascara(cliente[3] or '')
        campos['cpf_cnpj'].insert(0, cpf_cnpj_formatado)
        campos['telefone'].delete(0, tk.END)
        campos['telefone'].insert(0, cliente[4] or '')
        campos['cep'].delete(0, tk.END)
        campos['cep'].insert(0, cliente[5] or '')
        campos['endereco'].delete(0, tk.END)
        campos['endereco'].insert(0, cliente[6] or '')
        campos['numero'].delete(0, tk.END)
        campos['numero'].insert(0, cliente[7] or '')
        campos['complemento'].delete(0, tk.END)
        campos['complemento'].insert(0, cliente[8] or '')
        campos['bairro'].delete(0, tk.END)
        campos['bairro'].insert(0, cliente[9] or '')
        campos['cidade'].delete(0, tk.END)
        campos['cidade'].insert(0, cliente[10] or '')
        campos['uf'].delete(0, tk.END)
        campos['uf'].insert(0, cliente[11] or '')

def limpar_campos():
    global cliente_selecionado_id
    cliente_selecionado_id = None
    for campo in campos.values():
        campo.delete(0, tk.END)
    tree.selection_remove(tree.selection())

def aplicar_mascara_cpf_cnpj(event):
    # campo = event.widget
    # texto_atual = campo.get()
    # texto_formatado = util.aplicar_mascara(texto_atual)
    # if texto_formatado != texto_atual:
    #     posicao_cursor = campo.index(tk.INSERT)
    #     campo.delete(0, tk.END)
    #     campo.insert(0, texto_formatado)
    #     if posicao_cursor < len(texto_formatado):
    #         campo.icursor(posicao_cursor)
    #     else:
    #         campo.icursor(len(texto_formatado))
    campo = event.widget
    texto_atual = campo.get()
    posicao_cursor = campo.index(tk.INSERT)
    digitos_antes = len([c for c in texto_atual[:posicao_cursor] if c.isdigit()])
    texto_formatado = util.aplicar_mascara(texto_atual)
    if texto_formatado != texto_atual:
        campo.delete(0, tk.END)
        campo.insert(0, texto_formatado)
        nova_posicao = 0
        digitos_contados = 0
        for i, c in enumerate(texto_formatado):
            if c.isdigit():
                digitos_contados += 1
            if digitos_contados >= digitos_antes:
                nova_posicao = i + 1
                break
        else:
            nova_posicao = len(texto_formatado)
        campo.icursor(nova_posicao)
        

def aplicar_mascara_telefone(event):
    # campo = event.widget
    # texto_atual = campo.get()
    # texto_formatado = util.mascara_telefone(texto_atual)
    # if texto_formatado != texto_atual:
    #     posicao_cursor = campo.index(tk.INSERT)
    #     campo.delete(0, tk.END)
    #     campo.insert(0, texto_formatado)
    #     if posicao_cursor < len(texto_formatado):
    #         campo.icursor(posicao_cursor)
    #     else:
    #         campo.icursor(len(texto_formatado))
    campo = event.widget
    texto_atual = campo.get()
    posicao_cursor = campo.index(tk.INSERT)
    digitos_antes = len([c for c in texto_atual[:posicao_cursor] if c.isdigit()])
    texto_formatado = util.mascara_telefone(texto_atual)
    if texto_formatado != texto_atual:
        campo.delete(0, tk.END)
        campo.insert(0, texto_formatado)
        nova_posicao = 0
        digitos_contados = 0
        for i, c in enumerate(texto_formatado):
            if c.isdigit():
                digitos_contados += 1
            if digitos_contados >= digitos_antes:
                nova_posicao = i + 1
                break
        else:
            nova_posicao = len(texto_formatado)
        campo.icursor(nova_posicao)

def aplicar_mascara_cep(event):
    # campo = event.widget
    # texto_atual = campo.get()
    # texto_formatado = util.mascara_cep(texto_atual)
    # if texto_formatado != texto_atual:
    #     posicao_cursor = campo.index(tk.INSERT)
    #     campo.delete(0, tk.END)
    #     campo.insert(0, texto_formatado)
    #     if posicao_cursor < len(texto_formatado):
    #         campo.icursor(posicao_cursor)
    #     else:
    #         campo.icursor(len(texto_formatado))
    campo = event.widget
    texto_atual = campo.get()
    posicao_cursor = campo.index(tk.INSERT)
    digitos_antes = len([c for c in texto_atual[:posicao_cursor] if c.isdigit()])
    texto_formatado = util.mascara_cep(texto_atual)
    if texto_formatado != texto_atual:
        campo.delete(0, tk.END)
        campo.insert(0, texto_formatado)
        nova_posicao = 0
        digitos_contados = 0
        for i, c in enumerate(texto_formatado):
            if c.isdigit():
                digitos_contados += 1
            if digitos_contados >= digitos_antes:
                nova_posicao = i + 1
                break
        else:
            nova_posicao = len(texto_formatado)
        campo.icursor(nova_posicao)

def sair():
    resposta = messagebox.askyesno("Confirmar Saída", "Deseja sair da Tela de Clientes?")
    if resposta:
        janela.destroy()