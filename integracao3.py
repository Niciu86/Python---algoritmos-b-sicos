import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
df=pd.DataFrame({"Nome":["Ana","Raul","Marisa"],
                 "Idades":[22,33,44],
                 "Cidade":["Salvador","Recife","Manaus"]})
def mostrar(data):
    tree.delete(*tree.get_children())
    tree["columns"]=list(data.columns)
    tree["show"]="headings"
    
    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100,anchor="center")
    for _,row in data.iterrows():
        tree.insert("", "end",values=list(row))
        
    
def carregar_csv():
    caminho=filedialog.askopenfilename(title="Selecione o arquivo",filestypes=[("Arqrivos CSV","*.csv")])
    if caminho:
        try:
            df=pd.read_csv(caminho)
            mostrar(df)
        except Exception as e:
            tk.messagebox.showerror("Erro", "Não foi possível achar o arquivo")
            
main=tk.Tk()
main.title("Sistema Básico")
main.geometry("300x300")
tree=ttk.Treeview(main)
tree.pack(expand=True)
bt0=tk.Button(main,text="Exibir Dados",command=mostrar(df))
bt0.pack()
bt1=tk.Button(main,text="Carregar",command=carregar_csv)
bt1.pack()
main.mainloop()
