import tkinter 
from tkinter import ttk

# instanciei a janela
janela = tkinter.Tk()

# declaracao das variaveis
nome, telefone = tkinter.StringVar(), tkinter.StringVar()

def button_click():
  print(f"nome: {nome.get()}, telefone: {telefone.get()}")

ttk.Label(janela, text="Nome").grid(column=10, row=10)
ttk.Entry(janela, textvariable=nome).grid(column=20, row=10)
ttk.Label(janela, text="Telefone").grid(column=10, row=20)
ttk.Entry(janela, textvariable=telefone).grid(column=20, row=20)
ttk.Button(janela, text="Inserir", command=button_click).grid(column=20, row=30)


janela.title("Minha primeira aplicação")
janela.resizable(True, False)

janela.mainloop()