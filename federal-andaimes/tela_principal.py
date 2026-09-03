import tkinter as tk
from tkinter import messagebox
import sys
import os
try:
    import tela_clientes
    import tela_produtos
    import tela_nf
    import tela_bkp
except ImportError as e:
    print(f'Erro ao importar módulos: {e}')

janela_principal = None

def abrir_tela_principal():
    global janela_principal
    janela_principal = tk.Toplevel()
    janela_principal.title("Federal Andaimes")
    janela_principal.geometry("700x700")
    janela_principal.configure(bg='#ADD8E6')
    try:
        pasta_sistema = os.path.join(os.path.expanduser("~/Documents"), "Federal Andaimes - Sistema")
        caminho_icone = os.path.join(pasta_sistema, "icon.ico")
        if not os.path.exists(caminho_icone):
            caminho_icone = os.path.join(os.path.dirname(__file__), "icon.ico")
        if os.path.exists(caminho_icone):
            janela_principal.iconbitmap(caminho_icone)
    except:
        pass
    janela_principal.update_idletasks()
    x = (janela_principal.winfo_screenwidth() // 2) - (700 // 2)
    y = (janela_principal.winfo_screenheight() // 2) - (700 // 2)
    janela_principal.geometry(f"700x700+{x}+{y}")
    janela_principal.protocol("WM_DELETE_WINDOW", sair_sistema)
    criar_interface()

def criar_interface(): 
    frame_titulo = tk.Frame(janela_principal, bg='#ADD8E6')
    frame_titulo.pack(pady=(10, 10))   
    titulo = tk.Label(janela_principal, text="FEDERAL ANDAIMES", font=("Arial", 24, "bold"), bg='#ADD8E6', fg='#336699')
    titulo.pack(pady=(50, 30))
    frame_linha = tk.Frame(janela_principal, height=2, bg='#336699')
    frame_linha.pack(fill='x', padx=100, pady=(0, 20))
    frame_botoes = tk.Frame(janela_principal, bg='#ADD8E6')
    frame_botoes.pack(expand=True)
    criar_botoes(frame_botoes)
    frame_rodape = tk.Frame(janela_principal, bg="#add8e6")
    frame_rodape.pack(side='bottom', pady=15)
    rodape = tk.Label(janela_principal, text="Desenvolvido por Nickolas Markus da Silva Costa", font=("Arial", 10, "italic"), bg='#ADD8E6', fg='#505050')
    rodape.pack(side='bottom', pady=10)

def criar_botoes(parent):
    config_botao = {'width': 25, 'height': 2, 'font': ("Arial", 12, "bold"), 'cursor': 'hand2', 'relief': 'raised', 'bd': 2}
    btn_clientes = tk.Button(parent, text="Gerenciar Clientes", command=tela_clientes.abrir_tela_clientes, bg='#4682B4', fg='white', activebackground='#5a9bd5', **config_botao)
    btn_clientes.pack(pady=8)
    btn_produtos = tk.Button(parent, text="Gerenciar Produtos", command=tela_produtos.abrir_tela_produtos, bg="#B4B246", fg='white', activebackground='#5a9bd5', **config_botao)
    btn_produtos.pack(pady=8)
    btn_nf = tk.Button(parent, text="Nota Fatura", command=tela_nf.abrir_tela_nf, bg="#06A72E", fg='white', activebackground='#5a9bd5', **config_botao)
    btn_nf.pack(pady=8)
    btn_backup = tk.Button(parent, text="Backup", command=tela_bkp.abrir_tela_backup, bg="#58027A", fg='white', activebackground='#5a9bd5', **config_botao)
    btn_backup.pack(pady=8)
    btn_sair = tk.Button(parent, text="Sair", command=sair_sistema, bg='#DC143C', fg='white', activebackground='#5a9bd5', **config_botao)
    btn_sair.pack(pady=8)

def sair_sistema():
    resposta = messagebox.askyesno("Confirmar Saída", "Deseja realmente sair do sistema?")
    if resposta:
        print("Sistema encerrado com sucesso!")
        janela_principal.quit()
        janela_principal.destroy()
        sys.exit(0)

def fechar_janela():
    sair_sistema()
