from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkcalendar import Calendar, DateEntry
from datetime import date
from PIL import ImageTk, Image
from view import *


#Cores
preto = "#2e2d2b"
branco = "#feffff"
cinza = "#e5e5e5"
verde = "#00a095"
letra = "#403d3d"
azul = "#003452"
vermelho = "#ef5350"
azul2 = "#038cfc"

#Janela
janela = Tk()
janela.title("")
janela.geometry("850x620")
janela.configure(background=branco)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

#Frames
frame_logo = Frame(janela, width=850, height=52, bg=azul2)
frame_logo.grid(row=0, column=0, pady=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=branco)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=branco)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=branco)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

#Logo
app_logo = Label(frame_logo, text="Cadastro de alunos", width=850, height=52, pady=10, padx=325, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=azul2, fg=branco)
app_logo.place(x=0, y=0)

#Funçoes
#cadastrar alunos
def alunos():

    def novo_aluno():
        global imagem, imagem_strig, l_imagem

        nome = e_nome_aluno.get()
        email = e_email_aluno.get()
        telefone = e_telefone_aluno.get()
        sexo = c_sexo.get()
        data = data_nascimento.get()
        cpf = e_cpf_aluno.get()
        turma = c_turma_aluno.get()
        imagem = imagem_strig

        lista = [nome, email, telefone, sexo, imagem, data, cpf, turma]

        for i in lista:
            if i == '':
                messagebox.showerror('Erro', "Preencha todos os campos")
                return
        
        criar_alunos(lista)
        messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso')

        e_nome_aluno.destroy(0, END)
        e_email_aluno.destroy(0, END)
        e_telefone_aluno.destroy(0, END)
        c_sexo.destroy(0, END)
        data_nascimento.gedestroy(0, END)
        e_cpf_aluno.gedestroy(0, END)
        c_turma_aluno.destroy(0, END)

        mostrar_alunos()

    def update_aluno():
        global imagem, imagem_strig, l_imagem

        try:
            tree_itens = tree_aluno.focus()
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            e_nome_aluno.delete(0, END)
            e_email_aluno.delete(0, END)
            e_telefone_aluno.delete(0, END)
            c_sexo.delete(0, END)
            data_nascimento.delete(0, END)
            e_cpf_aluno.delete(0, END)
            c_turma_aluno.delete(0, END)

            e_nome_aluno.insert(0, tree_lista[1])
            e_email_aluno.insert(0, tree_lista[2])
            e_telefone_aluno.insert(0, tree_lista[3])
            c_sexo.insert(0, tree_lista[4])
            data_nascimento.insert(0, tree_lista[6])
            e_cpf_aluno.insert(0, tree_lista[7])
            c_turma_aluno.insert(0, tree_lista[8])

            imagem =tree_lista[5]
            imagem_strig = imagem

            imagem = Image.open(imagem)
            imagem = imagem.resize((130, 130))
            imagem = ImageTk.PhotoImage(imagem)
            l_imagem = Label(frame_detalhes, image=imagem, bg=branco, fg=preto)
            l_imagem.place(x=300, y=10)

            def update():
                global imagem, imagem_strig, l_imagem

                nome = e_nome_aluno.get()
                email = e_email_aluno.get()
                telefone = e_telefone_aluno.get()
                sexo = c_sexo.get()
                data = data_nascimento.get()
                cpf = e_cpf_aluno.get()
                turma = c_turma_aluno.get()
                imagem = imagem_strig

                lista = [nome, email, telefone, sexo, imagem, data, cpf, turma]

                for i in lista:
                    if i == '':
                        messagebox.showerror('Erro', "Preencha todos os campos")
                        return
                
                atualizar_aluno(lista)
                messagebox.showinfo('Sucesso', 'Dados atualizados com sucesso')

                e_nome_aluno.destroy(0, END)
                e_email_aluno.destroy(0, END)
                e_telefone_aluno.destroy(0, END)
                c_sexo.destroy(0, END)
                data_nascimento.gedestroy(0, END)
                e_cpf_aluno.gedestroy(0, END)
                c_turma_aluno.destroy(0, END)

                mostrar_alunos()

                botao_update.destroy()

            botao_update = Button(frame_detalhes, command=update, text="Salvar", width=10, overrelief=RIDGE, font=('Ivy 7'), bg=verde, fg=branco)
            botao_update.place(x=727, y=130)
        except IndexError:
            messagebox.showerror('Erro', 'Selecione uma dos alunos na tabela')

    def delete_aluno():
        try:
            tree_itens = tree_aluno.focus
            tree_dicionario = tree_aluno.item(tree_itens)
            tree_lista = tree_dicionario['values']
            
            valor_id = tree_lista[0]

            deletar_aluno([valor_id])

            messagebox.showinfo('Sucesso', 'Aluno excluido com sucesso')
            mostrar_alunos()
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um aluno na tabela')


    #Campos de entrada
    l_nome_aluno = Label(frame_detalhes, text="Nome", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_nome_aluno.place(x=4, y=10)
    e_nome_aluno = Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_nome_aluno.place(x=7, y=40)

    l_email_aluno = Label(frame_detalhes, text="E-mail", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_email_aluno.place(x=4, y=70)
    e_email_aluno = Entry(frame_detalhes, width=45, justify='left', relief='solid')
    e_email_aluno.place(x=7, y=100)

    l_telefone_aluno = Label(frame_detalhes, text="Telefone", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_telefone_aluno.place(x=4, y=130)
    e_telefone_aluno = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_telefone_aluno.place(x=7, y=160)

    #Seleção de genero
    l_sexo_aluno = Label(frame_detalhes, text="Sexo", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_sexo_aluno.place(x=190, y=130)

    c_sexo = ttk.Combobox(frame_detalhes, width=12, font=('Ivy 8 bold'))
    c_sexo['value'] = ('Masculino', 'Feminino', 'Trasexual', 'Bisexual', 'Outro', 'Não declarado')
    c_sexo.place(x=190, y=160)

    l_data_nascimento = Label(frame_detalhes, text="Data de nascimento", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_data_nascimento.place(x=446, y=10)
    data_nascimento = DateEntry(frame_detalhes, width=18, background='darkblue', foreground='white', borderwidth=2, year=2023)
    data_nascimento.place(x=450, y=40)

    l_cpf_aluno = Label(frame_detalhes, text="CPF", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_cpf_aluno.place(x=446, y=70)
    e_cpf_aluno = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_cpf_aluno.place(x=450, y=100)

    #Seleção do curso escolhido pelo aluno
    l_curso_aluno = Label(frame_detalhes, text="Turma", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_curso_aluno.place(x=446, y=130)

    turmas = ver_turmas()
    turma =[]

    for i in turmas:
        turma.append(i)

    c_turma_aluno = ttk.Combobox(frame_detalhes, width=12, font=('Ivy 8 bold'))
    c_turma_aluno['value'] = (turma)
    c_turma_aluno.place(x=450, y=160)

    #Função para seleção de imagem
    global imagem, imagem_strig, l_imagem

    def escolher_imagem():
        global imagem, imagem_strig, l_imagem

        imagem = fd.askopenfilename()
        imagem_strig = imagem

        imagem = Image.open(imagem)
        imagem = imagem.resize((130, 130))
        imagem = ImageTk.PhotoImage(imagem)
        l_imagem = Label(frame_detalhes, image=imagem, bg=branco, fg=preto)
        l_imagem.place(x=300, y=10)

        botao_carregar['text'] = 'Alterar foto'

    botao_carregar = Button(frame_detalhes, command=escolher_imagem, text="Carregar foto", width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg=azul2, fg=branco)
    botao_carregar.place(x=300, y=160)

    #Linha_divisoria
    l_linha = Label(frame_detalhes, relief=GROOVE, text="h", width=1, height=100, anchor=NW, font='Ivy 1', bg=preto, fg=preto)
    l_linha.place(x=610, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text="h", width=1, height=100, anchor=NW, font='Ivy 1', bg=branco, fg=preto)
    l_linha.place(x=608, y=10)

    #procurar alunos
    l_nome = Label(frame_detalhes, text='Procurar aluno', height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_nome.place(x=627, y=10)
    e_nome_procurar = Entry(frame_detalhes, width=17, justify='center', relief='solid', font=('Ivy 10'))
    e_nome_procurar.place(x=630, y=35)

    botao_procurar = Button(frame_detalhes, anchor=CENTER, text='Procurar', width=9, overrelief=RIDGE, font=('Ivy 7'), bg=azul2, fg=branco)
    botao_procurar.place(x=757, y=35)

    #Botões
    botao_salvar = Button(frame_detalhes, command=novo_aluno, text="Salvar", width=10, overrelief=RIDGE, font=('Ivy 7'), bg=verde, fg=branco)
    botao_salvar.place(x=627, y=120)

    botao_atualizar = Button(frame_detalhes, command=update_aluno, text="Atualizar", width=10, overrelief=RIDGE, font=('Ivy 7'), bg=azul2, fg=branco)
    botao_atualizar.place(x=627, y=140)

    botao_deletar = Button(frame_detalhes, command=delete_aluno, text="Deletar", width=10, overrelief=RIDGE, font=('Ivy 7'), bg=vermelho, fg=branco)
    botao_deletar.place(x=627, y=160)  

    botao_ver = Button(frame_detalhes, text="Ver", width=10, overrelief=RIDGE, font=('Ivy 7'), bg=azul2, fg=branco)
    botao_ver.place(x=757, y=160)


     #Tabela turma
    def mostrar_alunos():
        app_nome = Label(frame_tabela, text="Tabela de alunos", height=1, padx=0, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=branco, fg=preto)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #Treeview com duas scrolbar
        list_header = ['ID', 'Nome', 'email', 'Telefone', 'Sexo', 'Imagem', 'Data', 'CPF', 'Curso']
        df_list = ver_alunos()

        global tree_aluno

        tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended", columns=list_header, show="headings")
        vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
        hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)
        tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela.grid_rowconfigure(0, weight=12)

        hd = ['nw', 'nw', 'nw', 'center', 'center', 'center', 'center', 'center', 'center']
        h = [40, 150, 150, 70, 70, 70, 80, 80, 100]
        n = 0

        for col in list_header:
            tree_aluno.heading(col, text=col.title(), anchor=NW)
            #ajuste das colunas com o header
            tree_aluno.column(col,width=h[n], anchor=hd[n])
            n+=1

        for item in df_list:
            tree_aluno.inser(", 'end', values=item")
        

    mostrar_alunos()



#adicionar cursos e turmas
def adicionar():
    frame_tabela_curso =  Frame(frame_tabela, width=300, height=200, bg=branco)
    frame_tabela_curso.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

    frame_tabela_linha =  Frame(frame_tabela, width=30, height=200, bg=branco)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

    frame_tabela_turma =  Frame(frame_tabela, width=300, height=200, bg=branco)
    frame_tabela_turma.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

    #Sessão do curso -------------------------------------------------------

    def novo_curso():
        nome = e_nome_curso.get()
        duracao = e_duracao_curso.get()
        preco = e_preco_curso.get()

        lista = [nome, duracao, preco]

        for i in lista:
            if i == "":
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        
        criar_curso(lista)
        messagebox.showinfo('Sucesso', 'O dados foram salvos com sucesso')

        e_nome_curso.delete(0, END)
        e_duracao_curso.delete(0, END)
        e_preco_curso.delete(0, END)

        #Exibindo cursos


    def update_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            e_nome_curso.insert(0, tree_lista[1])
            e_duracao_curso.insert(0, tree_lista[2])
            e_preco_curso.insert(0, tree_lista[3])

            def update():
                nome = e_nome_curso.get()
                duracao = e_duracao_curso.get()
                preco = e_preco_curso.get()

                lista = [nome, duracao, preco, valor_id]

                for i in lista:
                    if i == "":
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return
                
                atualizar_curso(lista)
                messagebox.showinfo('Sucesso', 'O dados foram salvos com sucesso')

                e_nome_curso.delete(0, END)
                e_duracao_curso.delete(0, END)
                e_preco_curso.delete(0, END)

                mostrar_cursos()
                botao_confirmar_salvar.destroy()
            
            botao_confirmar_salvar = Button(frame_detalhes, command=update, text="Salvar atualização", overrelief=RIDGE, font=('Ivy 7'), bg=verde, fg=branco)
            botao_confirmar_salvar.place(x=227, y=130)
        except IndexError:
            messagebox.showerror('Erro', 'Selecione uma doss cursos na tabela')


    def delete_curso():
        try:
            tree_itens = tree_curso.focus()
            tree_dicionario = tree_curso.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            deletar_curso([valor_id])
            messagebox.showinfo('Os dados foram excluidos com sucesso')
            mostrar_cursos()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos cursos na tabela')



    l_nome = Label(frame_detalhes, text="Nome do curso", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_nome.place(x=4, y=10)
    e_nome_curso = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_curso.place(x=7, y=40)

    l_duracao = Label(frame_detalhes, text="Duração", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_duracao.place(x=4, y=70)
    e_duracao_curso = Entry(frame_detalhes, width=20, justify='left', relief='solid')
    e_duracao_curso.place(x=7, y=100)

    l_preco = Label(frame_detalhes, text="Preço", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_preco.place(x=4, y=130)
    e_preco_curso = Entry(frame_detalhes, width=10, justify='left', relief='solid')
    e_preco_curso.place(x=7, y=160)

    #botões

    botao_salvar = Button(frame_detalhes, command=novo_curso, text="Salvar", width=10, overrelief=RIDGE, font=('Ivy 7'), bg=verde, fg=branco)
    botao_salvar.place(x=90, y=160)

    botao_atualizar = Button(frame_detalhes, command=update_curso, text="Atualizar", width=10, overrelief=RIDGE, font=('Ivy 7'), bg=azul2, fg=branco)
    botao_atualizar.place(x=160, y=160)

    botao_deletar = Button(frame_detalhes, command=delete_curso, text="Deletar", width=10, overrelief=RIDGE, font=('Ivy 7'), bg=vermelho, fg=branco)
    botao_deletar.place(x=230, y=160)   


    #Tabela cursos
    def mostrar_cursos():
        app_nome = Label(frame_tabela_curso, text="Tabela de curso", height=1, padx=0, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=branco, fg=preto)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #Treeview com duas scrolbar
        list_header = ['ID', 'Curso', 'Duração', 'Preço']
        df_list = ver_curso()

        global tree_curso

        tree_curso = ttk.Treeview(frame_tabela_curso, selectmode="extended", columns=list_header, show="headings")
        vsb = ttk.Scrollbar(frame_tabela_curso, orient="vertical", command=tree_curso.yview)
        hsb = ttk.Scrollbar(frame_tabela_curso, orient="horizontal", command=tree_curso.xview)
        tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_curso.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_curso.grid_rowconfigure(0, weight=12)

        hd = ['nw', 'nw', 'e', 'e']
        h = [30, 150, 80, 60]
        n = 0

        for col in list_header:
            tree_curso.heading(col, text=col.title(), anchor=NW)
            #ajuste das colunas com o header
            tree_curso.column(col,width=h[n], anchor=hd[n])
            n+=1

        for item in df_list:
            tree_curso.inser(", 'end', values=item")
        

    mostrar_cursos()


    #Linhas separatorias
    l_linha = Label(frame_detalhes, relief=GROOVE, text="h", width=1, height=100, anchor=NW, font='Ivy 1', bg=preto, fg=preto)
    l_linha.place(x=374, y=10)
    l_linha = Label(frame_detalhes, relief=GROOVE, text="h", width=1, height=100, anchor=NW, font='Ivy 1', bg=branco, fg=preto)
    l_linha.place(x=372, y=10)

    l_linha = Label(frame_tabela_linha, relief=GROOVE, text="h", width=1, height=140, anchor=NW, font='Ivy 1', bg=preto, fg=preto)
    l_linha.place(x=6, y=10)
    l_linha = Label(frame_tabela_linha, relief=GROOVE, text="h", width=1, height=140, anchor=NW, font='Ivy 1', bg=branco, fg=preto)
    l_linha.place(x=4, y=10)

    #Sessão da turma ---------------------------------------------------

    def nova_turma():
        nome = e_nome_turma.get()
        curso = c_curso.get()
        data = data_inicio.get()

        lista = [nome, curso, data]

        for i in lista:
            if i == "":
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        
        criar_turmas(lista)
        messagebox.showinfo('Sucesso', 'O dados foram salvos com sucesso')

        e_nome_turma.delete(0, END)
        c_curso.delete(0, END)
        data_inicio.delete(0, END)

        mostrar_turmas()

    def update_turma():
        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            e_nome_turma.insert(0, tree_lista[1])
            c_curso.insert(0, tree_lista[2])
            data_inicio.insert(0, tree_lista[3])

            def update():
                nome = e_nome_turma.get()
                curso = c_curso.get()
                data = data_inicio.get()

                lista = [nome, curso, data, valor_id]

                for i in lista:
                    if i == "":
                        messagebox.showerror('Erro', 'Preencha todos os campos')
                        return
                
                atualizar_turmas(lista)
                messagebox.showinfo('Sucesso', 'O dados foram salvos com sucesso')

                e_nome_turma.delete(0, END)
                c_curso.delete(0, END)
                data_inicio.delete(0, END)

                mostrar_turmas()
                botao_confirmar_salvar.destroy()
            
            botao_confirmar_salvar = Button(frame_detalhes, command=update, text="Salvar atualização", overrelief=RIDGE, font=('Ivy 7'), bg=verde, fg=branco)
            botao_confirmar_salvar.place(x=407, y=130)
        except IndexError:
            messagebox.showerror('Erro', 'Selecione uma das turmas na tabela')

    def delete_turma():
        try:
            tree_itens = tree_turma.focus()
            tree_dicionario = tree_turma.item(tree_itens)
            tree_lista = tree_dicionario['values']

            valor_id = tree_lista[0]

            deletar_turmas([valor_id])
            messagebox.showinfo('Os dados foram excluidos com sucesso')
            mostrar_turmas()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione uma das turmas na tabela')


    l_nome = Label(frame_detalhes, text="Nome da turma", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_nome.place(x=404, y=10)
    e_nome_turma = Entry(frame_detalhes, width=35, justify='left', relief='solid')
    e_nome_turma.place(x=407, y=40)

    l_curso = Label(frame_detalhes, text="Curso", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_curso.place(x=404, y=70)

    cursos = ver_turmas()
    curso = []

    for i in cursos:
        curso.append(i[1])

    c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
    c_curso['value'] = (curso)
    c_curso.place(x=407, y=100)

    l_data_inicio = Label(frame_detalhes, text="Data de inicio", height=1, anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
    l_data_inicio.place(x=406, y=130)
    data_inicio = DateEntry(frame_detalhes, width=10, background='darkblue', foreground='white', borderwidth=2, year=2023)
    data_inicio.place(x=407, y=160)

    #botões

    botao_salvar = Button(frame_detalhes, command=nova_turma, text="Salvar", width=10, overrelief=RIDGE, font=('Ivy 7'), bg=verde, fg=branco)
    botao_salvar.place(x=507, y=160)

    botao_atualizar = Button(frame_detalhes, command=update_turma, text="Atualizar", width=10, overrelief=RIDGE, font=('Ivy 7'), bg=azul2, fg=branco)
    botao_atualizar.place(x=577, y=160)

    botao_deletar = Button(frame_detalhes, command=delete_turma, text="Deletar", width=10, overrelief=RIDGE, font=('Ivy 7'), bg=vermelho, fg=branco)
    botao_deletar.place(x=647, y=160)   

    #Tabela turma
    def mostrar_turmas():
        app_nome = Label(frame_tabela_turma, text="Tabela de turmas", height=1, padx=0, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=branco, fg=preto)
        app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        #Treeview com duas scrolbar
        list_header = ['ID', 'Nome da turma', 'Curso', 'Inicio']
        df_list = ver_turmas()

        global tree_turma

        tree_turma = ttk.Treeview(frame_tabela_turma, selectmode="extended", columns=list_header, show="headings")
        vsb = ttk.Scrollbar(frame_tabela_turma, orient="vertical", command=tree_turma.yview)
        hsb = ttk.Scrollbar(frame_tabela_turma, orient="horizontal", command=tree_turma.xview)
        tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree_turma.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_tabela_turma.grid_rowconfigure(0, weight=12)

        hd = ['nw', 'nw', 'e', 'e']
        h = [30, 130, 150, 80]
        n = 0

        for col in list_header:
            tree_turma.heading(col, text=col.title(), anchor=NW)
            #ajuste das colunas com o header
            tree_turma.column(col,width=h[n], anchor=hd[n])
            n+=1

        for item in df_list:
            tree_turma.inser(", 'end', values=item")
        

    mostrar_turmas()




#Salvar
def salvar():
    print('Salvar')


def controle(i):
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        alunos()
    elif i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        adicionar()
    elif i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        for widget in frame_tabela.winfo_children():
            widget.destroy()
        salvar()
    else:
        pass
        
    

#Botões
app_cadastro = Button(frame_dados, command=lambda:controle('cadastro'), text="Cadastrar", width=10, overrelief=RIDGE, font=('Ivy 11 bold'), bg=azul2, fg=branco)
app_cadastro.place(x=10, y=30)

app_adicionar = Button(frame_dados, command=lambda:controle('adicionar'), text="Adicionar", width=10, overrelief=RIDGE, font=('Ivy 11 bold'), bg=azul2, fg=branco)
app_adicionar.place(x=110, y=30)

app_salvar = Button(frame_dados, command=lambda:controle('salvar'), text="Salvar", width=10, overrelief=RIDGE, font=('Ivy 11 bold'), bg=azul2, fg=branco)
app_salvar.place(x=210, y=30)

alunos()
janela.mainloop()