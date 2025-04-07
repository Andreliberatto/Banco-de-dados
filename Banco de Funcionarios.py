import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime
import sqlite3


conn = sqlite3.connect("registro_ponto.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    departamento TEXT,
    data TEXT,
    hora_entrada TEXT,
    hora_saida TEXT
)
''')
conn.commit()

def registrar_ponto():
    """Registra o ponto com data e hora automática no banco de dados."""
    nome = nome_entry.get()
    departamento = departamento_combobox.get()

    if not nome or not departamento:
        messagebox.showerror("Erro", "Por favor, preencha o nome e selecione o departamento.")
        return

    agora = datetime.now()
    data_atual = agora.strftime("%Y-%m-%d")  # Formata a data como string
    hora_atual = agora.strftime("%H:%M:%S")  # Formata a hora como string


    cursor.execute("SELECT id FROM logs WHERE nome = ? AND data = ? AND hora_saida IS NULL", (nome, data_atual))
    resultado = cursor.fetchone()

    if resultado:
        # Atualiza a hora de saída
        cursor.execute("UPDATE logs SET hora_saida = ? WHERE id = ?", (hora_atual, resultado[0]))
        messagebox.showinfo("Sucesso", "Hora de saída registrada com sucesso!")
    else:
        # Insere um novo registro de entrada
        cursor.execute("INSERT INTO logs (nome, departamento, data, hora_entrada) VALUES (?, ?, ?, ?)",
                       (nome, departamento, data_atual, hora_atual))
        messagebox.showinfo("Sucesso", "Hora de entrada registrada com sucesso!")

    conn.commit()
    atualizar_logs()

def atualizar_logs():
    """Atualiza a exibição dos logs de acesso na interface a partir do banco de dados."""
    for item in log_tree.get_children():
        log_tree.delete(item)

    cursor.execute("SELECT nome, departamento, data, hora_entrada, hora_saida FROM logs")
    for log in cursor.fetchall():
        log_tree.insert("", "end", values=log)

def exportar_csv():
    """Exporta os logs de acesso para um arquivo CSV."""
    cursor.execute("SELECT nome, departamento, data, hora_entrada, hora_saida FROM logs")
    logs = cursor.fetchall()

    if not logs:
        messagebox.showerror("Erro", "Nenhum log disponível para exportar.")
        return

    try:
        with open("logs_acesso.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "Departamento", "Data", "Hora de Entrada", "Hora de Saída"])
            writer.writerows(logs)

        messagebox.showinfo("Sucesso", "Logs exportados para 'logs_acesso.csv' com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao exportar logs: {e}")

def adicionar_departamento():
    """Adiciona um novo departamento ao combobox dinamicamente."""
    novo_departamento = departamento_entry.get()
    if novo_departamento and novo_departamento not in departamento_combobox['values']:
        valores_atuais = list(departamento_combobox['values'])
        valores_atuais.append(novo_departamento)
        departamento_combobox['values'] = valores_atuais
        messagebox.showinfo("Sucesso", f"Departamento '{novo_departamento}' adicionado com sucesso!")
        departamento_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Por favor, insira um nome de departamento válido e único.")


root = tk.Tk()
root.title("Registro de Ponto")
root.geometry("800x600")
root.configure(bg="#F0F4F8")


style = ttk.Style()
style.configure("Treeview", rowheight=25, font=("Arial", 10))
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#E8EFFC")
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TLabel", background="#F0F4F8", font=("Arial", 10))


frame_registro = tk.Frame(root, bg="#F0F4F8")
frame_registro.pack(pady=10)


nome_label = ttk.Label(frame_registro, text="Nome:")
nome_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
nome_entry = ttk.Entry(frame_registro, width=30)
nome_entry.grid(row=0, column=1, padx=5, pady=5)

departamento_label = ttk.Label(frame_registro, text="Departamento:")
departamento_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
departamento_combobox = ttk.Combobox(frame_registro, width=27, state="readonly")
departamento_combobox["values"] = ["RH", "TI", "Financeiro", "Comercial"]
departamento_combobox.grid(row=1, column=1, padx=5, pady=5)


registrar_button = ttk.Button(frame_registro, text="Registrar Ponto", command=registrar_ponto)
registrar_button.grid(row=2, columnspan=2, pady=10)


frame_logs = tk.Frame(root, bg="#F0F4F8")
frame_logs.pack(pady=10, fill="both", expand=True)


log_tree = ttk.Treeview(frame_logs, columns=("Nome", "Departamento", "Data", "Hora de Entrada", "Hora de Saída"), show="headings")
log_tree.heading("Nome", text="Nome")
log_tree.heading("Departamento", text="Departamento")
log_tree.heading("Data", text="Data")
log_tree.heading("Hora de Entrada", text="Hora de Entrada")
log_tree.heading("Hora de Saída", text="Hora de Saída")
log_tree.column("Nome", width=150)
log_tree.column("Departamento", width=150)
log_tree.column("Data", width=100)
log_tree.column("Hora de Entrada", width=150)
log_tree.column("Hora de Saída", width=150)
log_tree.pack(fill="both", expand=True, pady=10)


frame_botoes = tk.Frame(root, bg="#F0F4F8")
frame_botoes.pack(pady=10)

exportar_button = ttk.Button(frame_botoes, text="Exportar Logs para CSV", command=exportar_csv)
exportar_button.grid(row=0, column=0, padx=10)


departamento_entry = ttk.Entry(frame_botoes, width=20)
departamento_entry.grid(row=0, column=1, padx=5)
adicionar_departamento_button = ttk.Button(frame_botoes, text="Adicionar Departamento", command=adicionar_departamento)
adicionar_departamento_button.grid(row=0, column=2, padx=5)

tk.mainloop()

conn.close()
