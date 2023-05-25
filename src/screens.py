import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import src.connection as connection
import src.game as game

connection.connect()

def open_login(window = None):

    if window:
        window.destroy()

    root = Tk()
    root.iconbitmap("images/logo.ico")
    root.title("PyJa Cross")
    root.geometry("925x500+300+200")
    root.configure(bg = "#fff")
    root.resizable(False,False)


    #Colocando a imagem na tela
    img = PhotoImage( file='images/login.png')
    Label(root, image = img, bg = 'white').place(x=0,y=0)

    #localizando a area onde serao inseridas as informações
    frame = Frame (root, width = 350,height = 350, bg ="")
    frame.place(x = 480, y = 70)

    #localizando a palavra login no codigo
    heading = Label (frame, text ='Login', fg = '#3771A1', bg = 'white', font = ('microsoft Yahei UILight', 23, 'bold'))
    heading.place(x =130, y=5)

    #Colocando o nome Usuario na tela

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name =user.get()

        if name == '':
            user.insert(0, 'RA')

    user = Entry(frame, width = 25, fg = 'black', border  = 0, bg = "white", font = ('Microsoft YaHei UI Light', 11))
    user.place(x =30, y = 80)
    user.insert(0, 'RA')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width = 295, height = 2, bg ='black').place(x = 25, y =107)

    #Colocando Senha na tela
    def on_enter(e):
        senha.delete(0, 'end')

    def on_leave(e):    
        name = senha.get()
        if name == '':
            senha.insert(0, 'Senha')

    senha = StringVar()
    senha = Entry(frame,width = 25, fg = 'black', border  = 0, bg = "white", font = ('Microsoft YaHei UI Light', 11))
    senha.insert(0, 'Senha')
    senha.place(x =30, y = 150)
    senha.bind('<FocusIn>', on_enter)
    senha.bind('<FocusOut>', on_leave)

    Frame(frame, width = 295, height = 2, bg ='black').place(x = 25, y =177)

    #Conexão da Tela de Login com o Banco de Dados
    def func_login():
        ra = user.get()
        senha_usuario = senha.get()

        if len(ra) == 10:
            loginResult = connection.login(ra, senha_usuario)
            if loginResult["auth"]:
                open_choose_screen(loginResult, root)
            else:
                messagebox.showinfo("Erro","RA e/ou Senha inválidos")
        else:
            messagebox.showinfo("Erro", "RA inválido")


        # sqlLogin = "SELECT * FROM users WHERE user_ra = %s AND user_password = %s;"
        # if len(ra) == 10:
        #     cursor.execute(sqlLogin,(ra,senha_usuario))
        #     resultLogin = cursor.fetchone()
        # else:
        #     messagebox.showinfo("Erro","Erro: RA inválido")
            
        # if resultLogin:
        #     messagebox.showinfo("Sucesso","Login Efetuado com sucesso")
        # else:
        #     messagebox.showinfo("Erro", "RA ou Senha inválido")

        # connection.commit()
        # cursor.close()

    #Criando botao de login e area para pessoas que nao possuem cadastro

    Button(frame, width =39, pady = 7, text = 'Login', bg = '#3771A1', fg = 'white', border = 0,command=func_login).place(x =35, y =204)
    label = Label(frame, text= "Não possui uma cadastro?", fg = 'black', bg = 'white', font = ('Microsoft YaHei UI Light', 10))
    label.place(x = 58, y = 270)

    sign_up = Button( frame, width = 0, text = 'Cadastre-se', border = 0, bg = 'white', cursor = 'hand2',fg = '#57a1f8',font = ('Microsoft YaHei UI Light', 10),command=lambda: open_signin(root))
    sign_up.place(x = 220, y = 268)

    # inicia o loop principal do tkinte
    root.mainloop()

def open_signin(window = None):
    
    if window:
        window.destroy()

    root = Tk()
    root.iconbitmap("images/logo.ico")
    root.title("PyJa Cross")
    root.geometry("925x500+300+200")
    root.configure(bg = "#fff")
    root.resizable(False,False)


    #Colocando a imagem na tela
    img = PhotoImage( file='images/login.png')
    Label(root, image = img, bg = 'white').place(x=0,y=0)

    #localizando a area onde serao inseridas as informações
    frame = Frame (root, width = 350,height = 350, bg ="")
    frame.place(x = 480, y = 70)

    #localizando a palavra login no codigo
    heading = Label (frame, text ='Cadastro', fg = '#3771A1', bg = 'white', font = ('microsoft Yahei UILight', 23, 'bold'))
    heading.place(x =100, y=5)

    #Colocando o nome Usuario na tela

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name =user.get()

        if name == '':
            user.insert(0, 'RA')

    user = Entry(frame, width = 25, fg = 'black', border  = 0, bg = "white", font = ('Microsoft YaHei UI Light', 11))
    user.place(x =30, y = 80)
    user.insert(0, 'RA')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width = 295, height = 2, bg ='black').place(x = 25, y =107)

    #Colocando Senha na tela
    def on_enter(e):
        senha.delete(0, 'end')

    def on_leave(e):
        name = senha.get()
        if name == '':
            senha.insert(0, 'Senha')

    senha = StringVar()
    senha = Entry(frame,width = 25, fg = 'black', border  = 0, bg = "white", font = ('Microsoft YaHei UI Light', 11))
    senha.insert(0, 'Senha')
    senha.place(x =30, y = 150)
    senha.bind('<FocusIn>', on_enter)
    senha.bind('<FocusOut>', on_leave)

    Frame(frame, width = 295, height = 2, bg ='black').place(x = 25, y =177)

    #Colocando Nome na tela
    def on_enter(e):
        nome.delete(0, 'end')

    def on_leave(e):
        name = nome.get()
        if name == '':
            nome.insert(0, 'Senha')

    nome = StringVar()
    nome = Entry(frame,width = 25, fg = 'black', border  = 0, bg = "white", font = ('Microsoft YaHei UI Light', 11))
    nome.insert(0, 'Nome')
    nome.place(x =30, y = 220)
    nome.bind('<FocusIn>', on_enter)
    nome.bind('<FocusOut>', on_leave)

    Frame(frame, width = 295, height = 2, bg ='black').place(x = 25, y =247)

    #Config Geral do Banco de Dados (MySQL)
    def func_cadastro():
        ra = user.get()
        senha_usuario = senha.get()
        _nome = nome.get()

        signUpResult = connection.signup(ra, senha_usuario, _nome)

        if len(ra) == 10:
            if signUpResult["approved"]:
                messagebox.showinfo("Sucesso", "Cadasdtro realizado com sucesso")
            else:
                messagebox.showinfo("Erro", "Usuário já cadastrado")
        else:
            messagebox.showinfo("Erro", "RA inálido")

    #     sql = "SELECT * FROM users WHERE user_ra = %s;"
    #     if len(ra) == 10:
    #         cursor.execute(sql,(ra))
    #         result = cursor.fetchone()
    #     else:
    #         messagebox.showinfo("Erro","Erro: RA inválido")
            
    #     if result:
    #         messagebox.showinfo("Erro","Erro: usuário já cadastrado")
    #     else:
    # # Executar uma consulta SQL INSERT para inserir os dados do novo usuário
    #         sql = "INSERT INTO users (user_ra,user_password,user_name) VALUES (%s,%s,%s);"
    #         cursor.execute(sql,(ra,senha_usuario,nome))
    #         messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso")

    #     connection.commit()
    #     cursor.close()
    #Criando botao de login e area para pessoas que nao possuem cadastro

    Button(frame, width =39, pady = 7, text = 'Login', bg = '#3771A1', fg = 'white', border = 0, command=func_cadastro).place(x =35, y =274)
    label = Label(frame, text= "Ja possui um cadastro?", fg = 'black', bg = 'white', font = ('Microsoft YaHei UI Light', 10))
    label.place(x = 58, y = 320)

    sign_up = Button( frame, width = 0, text = 'Login', border = 0, bg = 'white', cursor = 'hand2',fg = '#57a1f8',font = ('Microsoft YaHei UI Light', 10),command=lambda: open_login(root))
    sign_up.place(x = 202, y = 318)

    # inicia o loop principal do tkinter
    root.mainloop()

def open_choose_screen(loginResult, window = None):

    if window:
        window.destroy()


    root = Tk()
    root.iconbitmap("images/logo.ico")
    root.title("PyJa Cross")
    root.geometry("925x500+300+200")
    root.configure(bg = "#fff")
    root.resizable(False, False)


    img = ImageTk.PhotoImage(Image.open('images/login.png').resize((350, 350)))
    Label(root, image=img, bg="white").place(x=300,y=20)

    heading = Label(root, text="Escolha o modo de jogo", fg="#3771A1", bg="white", font=('microsoft Yahei UILight',23, 'bold'))
    heading.place(x = 300, y = 5)

    def open_game(gameType, screen, gameTypeId):
        screen.destroy()

        game.run(gameType, loginResult, gameTypeId)

    Button(root, width=30, height=3, font=('microsoft Yahei UILight',15), text="PYTHON", bg="#3771A1", fg='white', border=0,command=lambda: open_game("python", root, 0)).place(x=150, y = 350)
    Button(root, width=30, height=3, font=('microsoft Yahei UILight',15), text="JAVA", bg="#3771A1", fg="white", border=0, command=lambda: open_game("java", root, 1)).place(x=500, y=350)

    root.mainloop()