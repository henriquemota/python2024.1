import tkinter as tk
from tkinter import ttk
import sqlite3 as conn
from os import path, getcwd

dbpath = path.join(getcwd(), "codigos", "db", "telefones.sqlite")

janela = tk.Tk()
janela.title("Minha primeira aplicação")
# janela.geometry("800x600")
janela.resizable(True, False)

nome, telefone, itens = tk.StringVar(), tk.StringVar(), tk.StringVar()

def inserir():
  with conn.connect(dbpath) as cx:
    query = "insert into contatos (nome, telefone) values (?,?);"
    cursor = cx.cursor()
    cursor.execute(query, (nome.get(), telefone.get()))
    print("dados inseridos com sucesso")
  ler()

def ler():
  with conn.connect(dbpath) as cx:
    query = "select nome from contatos;"
    cursor = cx.cursor()
    cursor.execute(query)
    dados = cursor.fetchall()
    s = ""
    for i in dados:
      s += i[0] + "\n"
    
    itens.set(s)
      
# inicializacao do componente label
ttk.Label(janela, text="Nome").grid(column=10, row=20)
ttk.Entry(janela, textvariable=nome).grid(column=20, row=20)
ttk.Label(janela, text="Telefone").grid(column=10, row=40)
ttk.Entry(janela, textvariable=telefone).grid(column=20, row=40)
ttk.Button(janela, text="Salvar", command=inserir).grid(column=20, row=60)
tk.Listbox(janela, listvariable=itens).grid(column=20, row=80)

janela.mainloop()
