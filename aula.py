import mysql.connector

conexao = mysql.connector.connect(host='localhost',   user='root',   password='SQL123',   database='bdyoutube',)

cursor = conexao.cursor()


# CRUD.CREATE
vnome_produto = "coca cola 300ml"
vvalor = 3
comando = f'insert into vendas (nome_produto, valor) values ("{vnome_produto}", {vvalor})'
#cursor.execute(comando)
#conexao.commit()


# CRUD.READ
comando = f'select * from vendas'
cursor.execute(comando)
resultado = cursor.fetchall() #executa a leitura do banco de dados
print(resultado)


# CRUD.UPDATE
vidvendas = 4
vvalor = 6
comando = f'update vendas set valor = {vvalor}  where idvendas = {vidvendas}'
cursor.execute(comando)
conexao.commit()


# CRUD.DELETE
vnome_produto = "coca cola 300ml"
vvalor = 6
comando = f'delete from vendas where nome_produto = "{vnome_produto}"'
cursor.execute(comando)
conexao.commit()



cursor.close()
conexao.close()
