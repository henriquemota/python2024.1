import sqlite3 as conn
from os import path, getcwd
dbpath = path.join(getcwd(), "codigos", "db", "telefones.sqlite")

def criar_db():
  with conn.connect(dbpath) as cx:
    query = """
      create table contatos (
        id integer primary key autoincrement,
        nome text not null,
        telefone text not null
      );
    """
    cursor = cx.cursor()
    cursor.execute(query)

def inserir(data = ()):
  with conn.connect(dbpath) as cx:
    query = "insert into contatos (nome, telefone) values (?,?);"
    cursor = cx.cursor()
    cursor.execute(query, data)
    print("dados inseridos com sucesso")

def alterar(data = ()):
  with conn.connect(dbpath) as cx:
    query = "update contatos set nome = ?, telefone = ? where id = ?;"
    cursor = cx.cursor()
    cursor.execute(query, data)
    print("dados alterados com sucesso")

def excluir(data = ()):
  with conn.connect(dbpath) as cx:
    query = "delete from contatos where id = ?;"
    cursor = cx.cursor()
    cursor.execute(query, data)
    print("dados excluídos com sucesso")

def listar():
  with conn.connect(dbpath) as cx:
    query = "select id, nome, telefone from contatos order by nome;"
    cursor = cx.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def tabela(data):
  print("ID       Nome          Telefone")
  for item in data:
    print(f"{item[0]}       {item[1]}         {item[2]}")

def menu():

  print("1 - inserir")
  print("2 - alterar")
  print("3 - excluir")
  print("4 - listar")
  print("Qualquer tecla para sair")

  opcao = input("informe a opcao desejada: ")
  if opcao == "1":
    nome = input("informe um nome: ")
    telefone = input("informe um telefone: ")
    inserir((nome, telefone))
    menu()
  elif opcao == "2":
    data = listar()
    tabela(data)
    id = input("informe o id que deseja alterar: ")
    nome = input("informe o novo nome: ")
    telefone = input("informe o novo telefone: ")
    alterar((nome, telefone, id))
    menu()
  elif opcao == "3":
    data = listar()
    tabela(data)
    id = input("informe o id que deseja excluir: ")
    excluir((id,))
    menu()
  elif opcao == "4":
    data = listar()
    tabela(data)
    menu()
  
if __name__ == "__main__":
  menu()