import sqlite3 #importação do pacote SQLite
con=sqlite3.connect("dados.db") #cria o data base
# criação de tabelas
with sqlite3.connect("dados.db") as con:
    cur=con.cursor() #criar um cursor para SQL!!!!
    cur.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        email TEXT NOT NULL);""")
with sqlite3.connect("dados.db") as con:
    cur=con.cursor() #criar um cursor para SQL!!!!!!
    cur.execute("""CREATE TABLE IF NOT EXISTS pedidos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        preco REAL NOT NULL);""")
#inserir dados
with sqlite3.connect("dados.db") as con:
    cur=con.cursor() #criar um cursor para SQL!!!!
    cur.execute("INSERT INTO usuarios(nome,idade,email) VALUES (?,?,?);",
                ("Ana",18,"ana@gmail.com"))
    novo_id=cur.lastrowid
    print(f"Usuário inserido com ID {novo_id}")
novo_usuarios=[("Raul",22,"r@gmail.com"),("Iris",33,"iris@gmail.com"),("Marcus",33,"m@gmail.com")]
with sqlite3.connect("dados.db") as con:
    cur=con.cursor() #criar um cursor para SQL!!!!
    cur.executemany("INSERT INTO usuarios(nome,idade,email) VALUES (?,?,?);",novo_usuarios)
    ultimo_id=cur.lastrowid
    print(f"{cur.rowcount} usuarios novos")
    #print(f"ID mais recente {ultimo_id}")
script="""INSERT INTO pedidos(nome_produto,quantidade,preco) VALUES ("Tomate",2,5);
INSERT INTO pedidos(nome_produto,quantidade,preco) VALUES ("Uva",5,9);
INSERT INTO pedidos(nome_produto,quantidade,preco) VALUES ("Abacate",10,12);
INSERT INTO pedidos(nome_produto,quantidade,preco) VALUES ("Laranja",20,7);
"""
with sqlite3.connect("dados.db") as con:
    cur=con.cursor()
    cur.executescript(script)
    #print(f"{cur.rowcount} novo itens")
with sqlite3.connect("dados.db") as con:
    cur=con.cursor() #criar um cursor para SQL!!!!
    cur.execute("INSERT INTO usuarios(nome,idade,email) VALUES (?,?,?);",
                ("Matheus",58,"mt@gmail.com"))
    novo_id=cur.lastrowid
    print(f"Usuário inserido com ID {novo_id}")
# consulta de dados
print("\nTabela Usuários\n")
with sqlite3.connect("dados.db") as con:
    cur=con.cursor()#cursor
    cur.execute("SELECT id,nome,idade,email FROM usuarios;")#seleção de atributos(colunas)
    linhas=cur.fetchall()#lista com todos os dados
    for linha in linhas:#repetição individual
        print(f"ID={linha[0]}|Nome ={linha[1]}|Idade={linha[2]}|Email={linha[3]}")
print("\nTabela Pedidos\n")
with sqlite3.connect("dados.db") as con:
    cur=con.cursor()#cursor
    cur.execute("SELECT id,nome_produto,quantidade,preco FROM pedidos;")#seleção de atributos(colunas)
    linhas=cur.fetchall()#lista com todos os dados
    for linha in linhas:#repetição individual
        print(f"ID={linha[0]}|Nome ={linha[1]}|Quantidade={linha[2]}|preço={linha[3]}")
#consulta pontual
with sqlite3.connect("dados.db") as con:
    cur=con.cursor()
    cur.execute("SELECT nome,email FROM usuarios WHERE id=?;",(5,))
    registro=cur.fetchone()
    if registro:
        print("\nNome do usuário: ",registro[0]," email: ",registro[1])
    else:
        print("\nvazio")
#consulta geral
with sqlite3.connect("dados.db") as con:
    cur=con.cursor()
    cur.execute("SELECT * FROM pedidos;")
    batch_size=3 
    while True:
        lote=cur.fetchmany(batch_size)
        if not lote:
            break
        for pedido in lote:
            print(pedido)
#consulta parametrizada
with sqlite3.connect('dados.db') as con:
    cur=con.cursor()
    nome_busca="%M%"
    cur.execute("SELECT * FROM usuarios WHERE nome LIKE ?;",(nome_busca,))
    resultados=cur.fetchall()
    print("\n",resultados)
#consulta por coluna
with sqlite3.connect("dados.db") as con:
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("SELECT * FROM usuarios;")
    for row in cur:
        print(row["nome"],row["email"])
#atualização
with sqlite3.connect('dados.db') as con:
    cur=con.cursor()
    cur.execute("UPDATE usuarios SET email=? WHERE id =?",("proprietario@gmail.com",2))
    cur.execute("SELECT * FROM usuarios;")
    batch_size=3 
    while True:
        lote=cur.fetchmany(batch_size)
        if not lote:
            break
        for pedido in lote:
            print(pedido)
print("\n")
#atualização em lotes
with sqlite3.connect("dados.db") as con:
    cur=con.cursor()
    cur.execute("UPDATE usuarios SET nome = ? WHERE email LIKE ?",("excluido","%mt%"))
    cur.execute("SELECT * FROM usuarios;")
    batch_size=3 
    while True:
        lote=cur.fetchmany(batch_size)
        if not lote:
            break
        for pedido in lote:
            print(pedido)
print("\n")
#remover dados
with sqlite3.connect("dados.db") as con:
    cur=con.cursor()
    cur.execute("DELETE FROM usuarios WHERE nome=?;",("excluido",))
    print(f"Linhas deletadas: {cur.rowcount}")
    cur.execute("SELECT * FROM usuarios;")
    batch_size=3 
    while True:
        lote=cur.fetchmany(batch_size)
        if not lote:
            break
        for pedido in lote:
            print(pedido)
cur.close()
con.close()
