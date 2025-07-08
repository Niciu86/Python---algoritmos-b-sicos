import tkinter as tk
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

def mostrar():
    print(lista_conv)

def criar():
    with sqlite3.connect("dados_conv.db") as con:
        cur=con.cursor()
        cur.execute('''CREATE TABLE convidados(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            email TEXT NOT NULL);''')
        
        
def gravar():
    with sqlite3.connect("dados_conv.db") as con:
        cur=con.cursor()
        cur.executemany("INSERT INTO convidados(nome,idade,email) VALUES (?,?,?);",lista_conv)
        con.commit()
        
        
b0=tk.Button(main,text="Criar Tabela",command=criar)
b0.pack()
b1=tk.Button(main,text="Inserir",command=inserir)
b1.pack()
b2=tk.Button(main,text="Mostrar",command=mostrar)
b2.pack()
b3=tk.Button(main,text="Grava no Banco",command=gravar)
b3.pack()
main.mainloop()