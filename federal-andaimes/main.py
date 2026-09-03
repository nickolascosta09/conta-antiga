# sistema desenvolvido por Nickolas Markus da Silva Costa com auxílio de Inteligência Artificial
# IA utilizada: Claude
import tkinter as tk
from tkinter import messagebox
import sys
import os
try:
    import db_manager
    import tela_principal
except ImportError as e:
    print(f'Erro ao importar módulos: {e}')
    sys.exit(1)

def criar_pastas():
    try:
        pasta_documentos = os.path.expanduser("~/Documents")
        pasta_sistema = os.path.join(pasta_documentos, "Federal Andaimes - Sistema")
        pasta_nf = os.path.join(pasta_sistema, "Nota Fatura")
        pasta_backups = os.path.join(pasta_sistema, "Backups")
        pasta_bkp_cliente = os.path.join(pasta_backups, "Clientes")
        pasta_bkp_produto = os.path.join(pasta_backups, "Produtos")
        pasta_bkp_nf = os.path.join(pasta_backups, "Notas")
        os.makedirs(pasta_sistema, exist_ok=True)
        os.makedirs(pasta_nf, exist_ok=True)
        os.makedirs(pasta_backups, exist_ok=True)
        os.makedirs(pasta_bkp_cliente, exist_ok=True)
        os.makedirs(pasta_bkp_produto, exist_ok=True)
        os.makedirs(pasta_bkp_nf, exist_ok=True)
        print(f"Pasta do sistema criada: {pasta_sistema}")
        print(f"Pasta de Nota Fatura criada: {pasta_nf}")
        print(f"Pasta de Backups criada: {pasta_backups}")
        return True
    except Exception as e:
        print(f"Erro ao criar pastas: {e}")
        return False
    
def iniciar_bd():
    try:
        print("Inicializando Banco de Dados...")
        db_manager.initialize_database()
        print("✓ Banco de dados inicializado com sucesso!")
        return True
    except Exception as e:
        messagebox.showerror("Erro Crítico", f"Erro ao inicializar Banco de Dados:\n\n{e}\n\nO sistema será encerrado!")
        return False

def load_screen(root):
    load = tk.Toplevel(root)
    load.title("")
    load.geometry("400x200")
    load.overrideredirect(True)
    x = (load.winfo_screenwidth() // 2) - 200
    y = (load.winfo_screenheight() // 2) - 100
    load.geometry(f"400x200+{x}+{y}")
    load.configure(bg='#ADD8E6')
    label_titulo = tk.Label(load, text="FEDERAL ANDAIMES", font=("Arial", 24, "bold"), bg="#ADD8E6", fg='#336699')
    label_titulo.pack(pady=40)
    label_carregando = tk.Label(load, text="Carregando...", font=("Arial", 12), bg="#ADD8E6", fg="#505050")
    label_carregando.pack()
    label_versao = tk.Label(load, text="Versão 1.0", font=("Arial", 9, "italic"), bg="#add8e6", fg='#707070')
    label_versao.pack(side='bottom', pady=10)
    load.update()
    return load

def iniciar_sistema():
    print("=" * 50)
    print("Federal Andaimes - Iniciando...")
    print("=" * 50)
    print("\nCriando pastas do sistema...")
    if not criar_pastas():
        print("⚠ Aviso: Não foi possível criar todas as pastas")
    print("✓ Pastas criadas")
    print("\nInicializando Banco de Dados...")
    if not iniciar_bd():
        return False
    print("\n" + "=" * 50)
    print("✓ Sistema iniciado com sucesso!")
    return True

def main():
    root = tk.Tk()
    root.withdraw()
    # if os.path.exists("icon.png"):
    #     root.iconbitmap("icon.ico")
    # load = load_screen(root)
    if not iniciar_sistema():
        messagebox.showerror("Erro", "Erro ao iniciar o sistema")
        root.destroy()
        # load.destroy()
    tela_principal.abrir_tela_principal()
    # if tela_principal.abrir_tela_principal():
    #     load.destroy()
    root.mainloop()

if __name__ == "__main__":
    main()
