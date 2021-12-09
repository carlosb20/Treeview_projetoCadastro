import sqlite3


def conequita():
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS pessoas (
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL,
                fome TEXT NOT NULL,
                endereco TEXT NOT NULL,
                email TEXT NOT NULL,
                uf TEXT NOT NULL,
                cidade TEXT NOT NULL,
                barrio TEXT NOT NULL);""")
    return conn

def desconecta(conn):
    conn.close()

def inserirdados(nome,cpf,fome,endereco,email,uf,cidade,barrio):
    conn = conequita()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO pessoas(nome,cpf,fome,endereco,email,uf,cidade,barrio)VALUES('{nome}','{cpf}','{fome}','{endereco}','{email}','{uf}','{cidade}','{barrio}')")
    conn.commit()
    desconecta(conn)

def lista_nome():
    conn = conequita()
    cursor = conn.cursor()
    cursor.execute('SELECT * from pessoas')

    return cursor.fetchall()

def deleta_nome(valor):
    conn = conequita()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM pessoas WHERE nome = '{valor}' ")
    conn.commit()
    desconecta(conn)







