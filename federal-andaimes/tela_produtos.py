import tkinter as tk
import os
from tkinter import ttk, messagebox
try:
    import db_produto
    import util
except ImportError as e:
    print(f'Erro ao importar módulos: {e}')

janela = None
tree = None
campos = {}
produto_selecionado_id = None

def abrir_tela_produtos():
    global janela, tree, campos
    janela = tk.Toplevel()
    janela.title("Gerenciamento de Produtos")
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
    frame_form = tk.LabelFrame(janela, text="Dados do Produto", padx=10, pady=10)
    frame_form.pack(fill='x', padx=10, pady=10)
    criar_campos_formulario(frame_form)
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=10)
    criar_botoes(frame_botoes)
    frame_busca = tk.LabelFrame(janela, text="Buscar Produto", padx=10, pady=10)
    frame_busca.pack(fill='x', padx=10, pady=5)
    criar_area_busca(frame_busca)
    criar_tabela_produtos(janela)
    limpar_campos()

def criar_campos_formulario(frame):
    global campos
    tk.Label(frame, text="Nome:*", font=("Arial", 10)).grid(row=0, column=0, sticky='w', pady=5)
    campos['nome'] = tk.Entry(frame, width=40, font=("Arial", 10))
    campos['nome'].grid(row=0, column=1, padx=5, pady=5, sticky='w')
    tk.Label(frame, text="Preço:", font=("Arial", 10)).grid(row=1, column=0, sticky='w', padx=(20, 0), pady=5)
    campos['preco'] = tk.Entry(frame, width=30, font=("Arial", 10))
    campos['preco'].grid(row=1, column=1, padx=5, pady=5, sticky='w')
    campos['preco'].bind('<KeyRelease>', aplicar_mascara_preco)
    campos['preco'].bind('<FocusIn>', focar_campo_preco)
    tk.Label(frame, text="Unidade:", font=("Arial", 10)).grid(row=2, column=0, sticky='w', pady=5)
    campos['unidade'] = tk.Entry(frame, width=25, font=("Arial", 10))
    campos['unidade'].grid(row=2, column=1, padx=5, pady=5, sticky='w')

def criar_botoes(frame):
    btn_salvar = tk.Button(frame, text="Salvar", command=salvar_produto, width=12, height=1, font=("Arial", 10), bg='#228B22', fg='white', cursor='hand2')
    btn_salvar.pack(side='left', padx=5)
    btn_excluir = tk.Button(frame, text="Excluir", command=excluir_produto, width=15, height=1, font=("Arial", 10), bg="#FF0000", fg='white', cursor='hand2')
    btn_excluir.pack(side='left', padx=5)
    btn_sair = tk.Button(frame, text="Sair", command=sair, width=12, height=1, font=("Arial", 10), bg="#E2FA06", fg='black', cursor='hand2')
    btn_sair.pack(side='left', padx=5)

def criar_area_busca(frame):
    tk.Label(frame, text="Nome:", font=("Arial", 10)).pack(side='left', padx=5)
    entry_busca = tk.Entry(frame, width=30, font=("Arial", 10))
    entry_busca.pack(side='left', padx=5)
    def buscar():
        buscar_produtos(entry_busca.get())
    entry_busca.bind('<Return>', lambda e: buscar())
    btn_buscar = tk.Button(frame, text="Buscar", command=buscar, width=12, height=1, font=("Arial", 10), bg='#4682B4', fg='white', cursor='hand2')
    btn_buscar.pack(side='left', padx=5)
    btn_listar = tk.Button(frame, text="Listar Todos", command=listar_todos, width=12, height=1, font=("Arial", 10), bg='#A9A9A9', fg='white', cursor='hand2')
    btn_listar.pack(side='left', padx=5)

def criar_tabela_produtos(parent):
    global tree
    frame_tree = tk.Frame(parent)
    frame_tree.pack(fill='both', expand=True, padx=10, pady=10)
    scrollbar = ttk.Scrollbar(frame_tree)
    scrollbar.pack(side='right', fill='y')
    tree = ttk.Treeview(frame_tree, columns=('ID', 'Nome', 'Valor', 'Unidade'), show='headings', height=15, yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)
    tree.heading('ID', text='ID')
    tree.heading('Nome', text='Nome')
    tree.heading('Valor', text='Valor')
    tree.heading('Unidade', text='Unidade')
    tree.column('ID', width=50, anchor='center')
    tree.column('Nome', width=300, anchor='w')
    tree.column('Valor', width=150, anchor='center')
    tree.column('Unidade', width=150, anchor='center')
    tree.pack(side='left', fill='both', expand=True)
    tree.bind('<<TreeviewSelect>>', selecionar_produto)

def salvar_produto():
    global produto_selecionado_id
    nome = campos['nome'].get().strip()
    preco_texto = campos['preco'].get().strip()
    preco = extrair_valor_monetario(preco_texto)
    unidade_raw = campos['unidade'].get().strip()
    unidade = colocar_maiusculo(unidade_raw)
    if produto_selecionado_id is None:
        if nome is None:
            messagebox.showwarning("Aviso","Nome é obrigatório!")
            campos['nome'].focus()
            return
        if preco < 0:
            messagebox.showwarning("Aviso", "Preço não pode ser negativo!")
            campos['preco'].focus()
            return
        sucesso, resultado = db_produto.inserir_produto(nome, preco, unidade)
        if sucesso:
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            limpar_campos()
        else:
            messagebox.showerror("Erro", f"Erro ao cadastrar produto:\n{resultado}")
    else:
        sucesso, mensagem = db_produto.atualizar_produto(produto_selecionado_id, nome, preco, unidade)
        if sucesso:
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
            limpar_campos()
            listar_todos()
        else:
            messagebox.showerror("Erro", f"Erro ao atualizar produto:\n{mensagem}")

def excluir_produto():
    global produto_selecionado_id
    if produto_selecionado_id is None:
        messagebox.showwarning("Aviso", "Selecione um produto na tabela para excluir.")
        return 
    nome = campos['nome'].get()
    resposta = messagebox.askyesno("Confirmar Exclusão", f"Deseja realmente excluir o produto '{nome}'?")
    if resposta:
        sucesso, mensagem = db_produto.excluir_produto(produto_selecionado_id)
    if sucesso:
        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
        limpar_campos()
        listar_todos()
    else:
        messagebox.showerror("Erro", f"Erro ao excluir produto:\n{mensagem}")

def buscar_produtos(nome_campo):
    nome = nome_campo.strip()
    if not nome_campo:
        messagebox.showinfo("Busca", "Digite um nome para buscar.")
        return
    for item in tree.get_children():
        tree.delete(item)
    produtos = db_produto.buscar_produtos(nome)
    if not produtos:
        messagebox.showinfo("Busca", f"Nenhum produto encontrado com o nome: {nome}")
        return
    for produto in produtos:
        preco_formatado = util.formatar_moeda(float(produto[2] or 0))
        tree.insert('', 'end', values=(produto[0], produto[1], preco_formatado, produto[3]))

def listar_todos():
    for item in tree.get_children():
        tree.delete(item)
    produtos = db_produto.listar_produtos()
    if not produtos:
        messagebox.showinfo("Informação", "Nenhum produto cadastrado.")
        return
    for produto in produtos:
        preco_formatado = util.formatar_moeda(float(produto[2] or 0))
        tree.insert('', 'end', values=(produto[0], produto[1], preco_formatado, produto[3]))

def selecionar_produto(event):
    global produto_selecionado_id
    selecionado = tree.selection()
    if not selecionado:
        return
    item = tree.item(selecionado[0])
    produto_id = item['values'][0]
    produto = db_produto.preencher_produtos(produto_id)
    if produto:
        produto_selecionado_id = produto[0]
        campos['nome'].delete(0, tk.END)
        campos['nome'].insert(0, produto[1] or '')
        campos['preco'].delete(0, tk.END)
        preco_formatado = util.formatar_moeda(float(produto[2] or 0))
        campos['preco'].insert(0, preco_formatado)
        campos['unidade'].delete(0, tk.END)
        campos['unidade'].insert(0, produto[3] or '')

def aplicar_mascara_preco(event):
    campo = event.widget
    texto_atual = campo.get()
    if not texto_atual or texto_atual == 'R$ ':
        return
    texto_formatado = util.mascara_moeda(texto_atual)
    if texto_formatado != texto_atual:
        posicao_cursor = campo.index(tk.INSERT)
        campo.delete(0, tk.END)
        campo.insert(0, texto_formatado)
        campo.icursor(tk.END)

def focar_campo_preco(event):
    campo = event.widget
    texto_atual = campo.get()
    if not texto_atual or texto_atual.strip() == '':
        campo.delete(0, tk.END)
        campo.insert(0, 'R$ 0,00')
        campo.select_range(0, tk.END)

def extrair_valor_monetario(texto):
    if not texto:
        return 0.0
    texto = texto.replace('R$', '').replace(' ', '').strip()
    texto = texto.replace('.', '').replace(',', '.')
    try:
        return float(texto)
    except ValueError:
        return 0.0

def limpar_campos():
    global produto_selecionado_id
    produto_selecionado_id = None
    campos['nome'].delete(0, tk.END)
    campos['preco'].delete(0, tk.END)
    campos['unidade'].delete(0, tk.END)
    tree.selection_remove(tree.selection())

def colocar_maiusculo(texto_raw):
    texto = texto_raw.upper()
    return texto

def sair():
    resposta = messagebox.askyesno("Confirmar Saída", "Deseja sair da Tela de Produtos?")
    if resposta:
        janela.destroy()