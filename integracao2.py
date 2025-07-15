import tkinter as tk
from tkinter import ttk
import sqlite3
lista_conv=[]
con=sqlite3.connect("dados_conv.db")

main=tk.Tk()
main.title("Sistema de convidados")
main.geometry("400x300")
label0=tk.Label(main,text="Olá Usuário!!!!")
label0.pack()
label1=tk.Label(main,text="Nome do convidado")
label1.pack()
entrada0=tk.Entry(main)
entrada0.pack()
label2=tk.Label(main,text="Idade do convidado")
label2.pack()
entrada1=tk.Entry(main)
entrada1.pack()
label3=tk.Label(main,text="Email do convidado")
label3.pack()
entrada2=tk.Entry(main)
entrada2.pack()

def inserir():
    nome=entrada0.get()
    idade=entrada1.get()
    email=entrada2.get()
    lista_conv.append((nome,idade,email))
    with sqlite3.connect("dados_conv.db") as con:
        cur=con.cursor()
        cur.executemany("INSERT INTO convidados(nome,idade,email) VALUES (?,?,?);",lista_conv)
        con.commit()
        
def mostrar():
    print(lista_conv)
    con=sqlite3.connect("dados_conv.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM convidados")
    registros=cur.fetchall()
    for item in tree.get_children():
        tree.delete(item)
    for linha in registros:
        tree.insert("", tk.END,values=linha)

def criar():
    with sqlite3.connect("dados_conv.db") as con:
        cur=con.cursor()
        cur.execute('''CREATE TABLE convidados(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT NOT NULL);''')

def deletar():
    item=tree.focus()
    
    valores=tree.item(item,"values")
    id_conv=valores[0]
    con=sqlite3.connect("dados_conv.db")
    cur=con.cursor()
    cur.execute("DELETE FROM convidados WHERE id=?",(id_conv,))
    con.commit()
    cur.execute("SELECT * FROM convidados")
    registros=cur.fetchall()
    for item in tree.get_children():
        tree.delete(item)
    for linha in registros:
        tree.insert("", tk.END, values=linha)
        
    cur.close()
    con.close()
    
        
b0=tk.Button(main,text="Criar Tabela",command=criar)
b0.pack()
b1=tk.Button(main,text="Inserir",command=inserir)
b1.pack()
b2=tk.Button(main,text="Mostrar",command=mostrar)
b2.pack()
colunas=("id","nome","idade","email")
tree=ttk.Treeview(main,columns=colunas,show="headings")
tree.heading("id", text="id")
tree.heading("nome", text="nome")
tree.heading("idade",text="idade")
tree.heading("email", text="email")
tree.pack(expand=True,fill=tk.BOTH)
b3=tk.Button(main,text="Deletar",command=deletar)
b3.pack()

main.mainloop()