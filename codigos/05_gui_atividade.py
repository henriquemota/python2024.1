import tkinter as tk
from tkinter import ttk
import sqlite3 as conn
from os import path, getcwd

dbpath = path.join(getcwd(), "codigos", "db", "telefones.sqlite")

janela = tk.Tk()
janela.title("Cadastro de contatos")
janela.resizable(False, False)

nome, telefone = tk.StringVar(), tk.StringVar()

def inserir():
  with conn.connect(dbpath) as cx:
    query = "insert into contatos (nome, telefone) values (?,?);"
    cursor = cx.cursor()
    cursor.execute(query, (nome.get(), telefone.get()))
  
  print("dados inseridos com sucesso")
  
def ler():
  with conn.connect(dbpath) as cx:
    query = "select nome, telefone from contatos;"
    cursor = cx.cursor()
    cursor.execute(query)
    dados = cursor.fetchall()
    
  with open("dados.txt", "w") as f:
    for dado in dados:
      f.writelines(dado[0] + "," + dado[1]  + "\n")
  
  print("dados exportados com sucesso")
      
ttk.Label(janela, text="Nome").grid(column=10, row=20)
ttk.Entry(janela, textvariable=nome).grid(column=20, row=20)
ttk.Label(janela, text="Telefone").grid(column=10, row=40)
ttk.Entry(janela, textvariable=telefone).grid(column=20, row=40)
ttk.Button(janela, text="Salvar", command=inserir).grid(column=10, row=60)
ttk.Button(janela, text="Gerar arquivo", command=ler).grid(column=20, row=60)

janela.mainloop()
