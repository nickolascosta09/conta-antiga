import tkinter as tk
from tkinter import messagebox
import os
try:
    import bkp
    import db_cliente
    import db_produto
except ImportError as e:
    print(f'Erro ao importar módulos: {e}')

janela = None
tree_clientes = None
tree_produtos = None
text_info = None

def abrir_tela_backup():
    global janela, tree_clientes, tree_produtos, text_info
    janela = tk.Toplevel()
    janela.title("Backup")
    janela.geometry("900x700")
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
    x = (janela.winfo_screenwidth() // 2) - (900 // 2)
    y = (janela.winfo_screenheight() // 2) - (700 // 2)
    janela.geometry(f"900x700+{x}+{y}")
    titulo = tk.Label(janela, text="Gerenciamento de Backups", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)
    criar_botoes(janela)
    info = tk.Label(janela, text="Os arquivos serão salvos na pasta:\nDocumentos / Federal Andaimes - Sistema / Backups", font=("Arial", 9), fg='#666666')
    info.pack(side='bottom', pady=20)

def criar_botoes(parent):
    # config_botao = {'width': 25, 'height': 2, 'font': ("Arial", 12, "bold"), 'cursor': 'hand2', 'relief': 'raised', 'bd': 2}
    btn_bkp_cliente = tk.Button(parent, text="Clientes", command=exportar_clientes, width=25, height=2, font=("Arial", 12, "bold"), bg="#000CB4", fg='white', activebackground='#5a9bd5', cursor='hand2', relief='raised', bd=2)
    btn_bkp_cliente.pack(pady=8)
    btn_bkp_produto = tk.Button(parent, text="Produtos", command=exportar_produtos, width=25, height=2, font=("Arial", 12, "bold"), bg="#ffe600", fg='black',activebackground='#5a9bd5', cursor='hand2', relief='raised', bd=2)
    btn_bkp_produto.pack(pady=8)
    # btn_bkp_nota = tk.Button(parent, text="Nota Fatura", command=exportar_notas, width=25, height=2, font=("Arial", 12, "bold"), bg="#FF8800", fg='white', activebackground='#5a9bd5', cursor='hand2', relief='raised', bd=2)
    # btn_bkp_nota.pack(pady=8)

def confirmar_exportar_clientes():
    resposta = messagebox.askyesno("Confirmar Exportação", "Deseja fazer backup dos clientes?\n\nO arquivo será salvo na pasta de backups em um arquivo .xlsx"
    )
    if resposta:
        exportar_clientes()

def confirmar_exportar_produtos():
    resposta = messagebox.askyesno("Confirmar Exportação", "Deseja fazer backup dos produtos?\n\nO arquivo será salvo na pasta de backups em um arquivo .xlsx"
    )
    if resposta:
        exportar_produtos()

# def confirmar_exportar_nota():
#     resposta = messagebox.askyesno("Confirmar Exportação", "Deseja fazer backup das Notas?\n\nO arquivo será salvo na pasta de backups em um arquivo .xlsx"
#     )
#     if resposta:
#         exportar_produtos()

def exportar_clientes():
    try:
        clientes = db_cliente.listar_clientes()
        if not clientes:
            messagebox.showinfo("Informação", "Nenhum cliente cadastrado para exportar.")
            return
        sucesso, resultado = bkp.exportar_clientes(clientes)
        if sucesso:
            nome_arquivo = os.path.basename(resultado)
            messagebox.showinfo("Arquivo gerado com sucesso!", f"Nome: {nome_arquivo}")
        else:
            messagebox.showerror("Erro", f"Erro ao exportar:\n{resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro inesperado:\n{str(e)}")

def exportar_produtos():
    try:
        produtos = db_produto.listar_produtos()
        if not produtos:
            messagebox.showinfo("Informação","Nenhum produto cadastrado para exportar.")
            return
        sucesso, resultado = bkp.exportar_produtos_xls(produtos)
        if sucesso:
            nome_arquivo = os.path.basename(resultado)
            messagebox.showinfo("Arquivo gerado com sucesso!", f"Nome: {nome_arquivo}\n")
        else:
            messagebox.showerror("Erro", f"Erro ao exportar:\n{resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro inesperado:\n{str(e)}")

# def exportar_notas():
#     try:
#         produtos = db_produto.listar_produtos()
#         if not produtos:
#             messagebox.showinfo("Informação","Nenhum produto cadastrado para exportar.")
#             return
#         sucesso, resultado = bkp.exportar_produtos_xls(produtos)
#         if sucesso:
#             nome_arquivo = os.path.basename(resultado)
#             messagebox.showinfo("Arquivo gerado com sucesso!", f"Nome: {nome_arquivo}\n")
#         else:
#             messagebox.showerror("Erro", f"Erro ao exportar:\n{resultado}")
#     except Exception as e:
#         messagebox.showerror("Erro", f"Erro inesperado:\n{str(e)}")