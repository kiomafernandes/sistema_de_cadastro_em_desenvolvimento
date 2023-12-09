import sqlite3 as lite

#Criando conexão com banco de dados
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexão com banco de dados realizdas com sucesso!')
except lite.Error as e:
    print('Erro ao conectar com o banco de dados:', e)


#Tabela cursos--------------------

#Criar cursos
def criar_curso(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO cursos (nome, duracao, preco) VALUE (?, ?, ?)'
        cur.execute(query, i)

#criar_cursos(['Algebra linear', '40 h', 50])

#Ver todos os cursos
def ver_curso():
    lista = []
    with con:
        cur = con.cursor
        cur.execute('SELECT * FROM cursos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista


#Atualizar cursos
def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE cursos SET nome=?, duracao=?, preco=? WHERE id=?'
        cur.execute(query, i)


#Deletar cursos
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM cursos WHERE id=?'
        cur.execute(query, i)


#Tabela de turmas---------------------------------

#Criar turmas
def criar_turmas(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO turmas (nome, turma_nome, data_inicio) VALUE (?, ?, ?)'
        cur.execute(query, i)


#ver turmas
def ver_turmas():
    lista = []
    with con:
        cur = con.cursor
        cur.execute('SELECT * FROM turmas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista


#Atualizar turmas
def atualizar_turmas(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE turmas SET nome=?, cursos_nome=?, data_inicio=? WHERE id=?'
        cur.execute(query, i)


#Deletar turmas
def deletar_turmas(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM turmas WHERE id=?'
        cur.execute(query, i)


#Tabela de alunos----------------------------------
#Criar alunos
def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUE (?, ?, ?, ?, ?, ?, ?, ?)'
        cur.execute(query, i)


#ver alunos
def ver_alunos():
    lista = []
    with con:
        cur = con.cursor
        cur.execute('SELECT * FROM alunos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista


#Atualizar alunos
def atualizar_aluno(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?'
        cur.execute(query, i)


#Deletar alunos
def deletar_aluno(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM alunos WHERE id=?'
        cur.execute(query, i)