from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import *
import datetime

import src.connection as connection
import src.game as game
from src.misc import *

colors = {
    "background": "#2B2D2E",
    "white": "#DDD",
    "theme": "#3771A1"
}

connection.connect()

def open_login(window = None):

    if window:
        window.destroy()

    root = Tk()
    root.iconbitmap("images/logo.ico")
    root.title("PyJa Cross")
    root.geometry("925x500+300+200")
    root.configure(bg = colors["background"])
    root.resizable(False,False)

    set_appearance_mode("Dark")


    #Colocando a imagem na tela
    img = PhotoImage( file='images/_logo.png')
    Label(root, image = img, bg = colors["background"]).place(x=0,y=0)

    #localizando a area onde serao inseridas as informações
    frame = Frame (root, width = 350,height = 350, bg ="")
    frame.place(x = 480, y = 70)

    #localizando a palavra login no codigo
    heading = Label (frame, text ='Login', fg = '#3771A1', bg = colors["background"], font = ('microsoft Yahei UILight', 23, 'bold'))
    heading.place(x =130, y=5)

    #Colocando o nome Usuario na tela

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name =user.get()

        if name == '':
            user.insert(0, 'RA')

    user = Entry(frame, width = 25, fg = colors["white"], border  = 0, bg = colors["background"], font = ('Microsoft YaHei UI Light', 11))
    user.place(x =30, y = 80)
    user.insert(0, 'RA')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width = 295, height = 2, bg =colors["white"]).place(x = 25, y =107)

    #Colocando Senha na tela
    def on_enter(e):
        senha.delete(0, 'end')

    def on_leave(e):    
        name = senha.get()
        if name == '':
            senha.insert(0, 'Senha')

    senha = StringVar()
    senha = Entry(frame,width = 25, fg = colors["white"], border  = 0, bg = colors["background"], font = ('Microsoft YaHei UI Light', 11))
    senha.insert(0, 'Senha')
    senha.place(x =30, y = 150)
    senha.bind('<FocusIn>', on_enter)
    senha.bind('<FocusOut>', on_leave)

    Frame(frame, width = 295, height = 2, bg =colors["white"]).place(x = 25, y =177)

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


    CTkButton(frame, width=270, height=40, text='Login',bg_color=colors["background"], fg_color=colors["theme"], corner_radius=5, text_color="white", command=func_login).place(x=35, y=204)
    label = Label(frame, text= "Não possui uma cadastro?", fg = colors["white"], bg = colors["background"], font = ('Microsoft YaHei UI Light', 10))
    label.place(x = 58, y = 270)

    sign_up = Button( frame, width = 0, text = 'Cadastre-se', border = 0, bg = colors["background"], cursor = 'hand2',fg = colors["theme"],font = ('Microsoft YaHei UI Light', 10),command=lambda: open_signin(root))
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
    root.configure(bg = colors["background"])
    root.resizable(False,False)


    #Colocando a imagem na tela
    img = PhotoImage( file='images/_logo.png')
    Label(root, image = img, bg = colors["background"]).place(x=10,y=0)

    #localizando a area onde serao inseridas as informações
    frame = Frame (root, width = 350,height = 350, bg =colors["background"])
    frame.place(x = 480, y = 70)

    #localizando a palavra login no codigo
    heading = Label (frame, text ='Cadastro', fg = '#3771A1', bg = colors["background"], font = ('microsoft Yahei UILight', 23, 'bold'))
    heading.place(x =100, y=5)

    #Colocando o nome Usuario na tela

    user = CTkEntry(frame, width = 250, text_color = "white", border_width  = 0, bg_color=colors["background"], fg_color = colors["background"], font = ('Microsoft YaHei UI Light', 14), placeholder_text="RA")
    user.place(x =25, y = 80)

    Frame(frame, width = 295, height = 2, bg =colors["white"]).place(x = 25, y =107)

    #Colocando Senha na tela
    def on_enter(e):
        senha.delete(0, 'end')


    senha = StringVar()
    senha = CTkEntry(frame,width = 250, text_color = "white", fg_color = colors["background"], font = ('Microsoft YaHei UI Light', 14), show="*", border_width=0, placeholder_text="Senha")
    senha.place(x =25, y = 150)

    Frame(frame, width = 295, height = 2, bg =colors["white"]).place(x = 25, y =177)

    #Colocando Nome na tela

    nome = StringVar()
    nome = CTkEntry(frame, width = 250, text_color = "white", border_width  = 0, bg_color=colors["background"], fg_color = colors["background"], font = ('Microsoft YaHei UI Light', 14), placeholder_text="Nome")
    nome.place(x =25, y = 220)

    Frame(frame, width = 295, height = 2, bg =colors["white"]).place(x = 25, y =247)

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

    CTkButton(frame, width=270, height=40, text='Cadastro',bg_color=colors["background"], fg_color=colors["theme"], corner_radius=5, text_color="white", command=func_cadastro).place(x=35, y=274)
    label = Label(frame, text= "Ja possui um cadastro?", fg = colors["white"], bg = colors["background"], font = ('Microsoft YaHei UI Light', 10))
    label.place(x = 58, y = 320)

    sign_up = Button( frame, width = 0, text = 'Login', border = 0, bg = colors["background"], cursor = 'hand2',fg = '#57a1f8',font = ('Microsoft YaHei UI Light', 10),command=lambda: open_login(root))
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
    root.configure(bg = colors["background"])
    root.resizable(False, False)


    img = ImageTk.PhotoImage(Image.open('images/_logo.png').resize((350, 350)))
    Label(root, image=img, bg=colors["background"]).place(x=300,y=20)

    heading = Label(root, text="Escolha o modo de jogo", fg="#3771A1", bg=colors["background"], font=('microsoft Yahei UILight',23, 'bold'))
    heading.place(x = 300, y = 5)

    def open_game(gameType, screen, gameTypeId):
        screen.destroy()

        game.run(gameType, loginResult, gameTypeId)

    Button(root, width=30, height=3, font=('microsoft Yahei UILight',15), text="PYTHON", bg="#3771A1", fg=colors["white"], border=0,command=lambda: open_game("python", root, 0)).place(x=150, y = 350)
    Button(root, width=30, height=3, font=('microsoft Yahei UILight',15), text="JAVA", bg="#3771A1", fg=colors["white"], border=0, command=lambda: open_game("java", root, 1)).place(x=500, y=350)

    root.mainloop()

def open_main_screen():
    root = Tk()
    root.iconbitmap("images/logo.ico")
    root.title("PyJa Cross")
    root.geometry("925x500+300+200")
    root.configure(bg = "#2B2D2E")
    root.resizable(False, False)

    set_appearance_mode("Dark")

    text = Label(root, text="Bem Vindo(a) ao PyJa Cross!", fg="#659FCF", bg="#2B2D2E", font = ('microsoft Yahei UILight', 23, 'bold'), justify=CENTER)
    text.place(x=250, y=20)

    buttonsFrame = Frame(root, width=300, height=350, bg="#2B2D2E")
    buttonsFrame.place(x = 10, y = 150)

    playButton = CTkButton(buttonsFrame, text="JOGAR", command=lambda: open_login(root), width=300, height=70, fg_color="#3771A1", corner_radius=10, text_color="#fff", font = ('sans-serif', 23, 'bold'))
    playButton.place(x = 0, y = 60)

    rankButton = CTkButton(buttonsFrame, text="RANKING", command=lambda: open_ranking(root), width=300, height=70, fg_color="#3771A1", corner_radius=10, text_color="#fff", font = ('sans-serif', 23, 'bold'))
    rankButton.place(x = 0, y = 170)

    img = ImageTk.PhotoImage(Image.open('images/_logo.png').resize((350, 350)))
    Label(root, image=img, bg="#2B2D2E").place(x=400,y=70)

    root.mainloop()

def open_ranking(window = None):
    
    if window:
        window.destroy()

    root = Tk()
    root.title("Tela de Ranks")
    root.geometry("925x500+300+200")

    root.resizable(0,0)
    root.config(bg=colors['background'])

    def generateRanks():
        times = connection.getTimes()
        ranks = []

        for i in range(len(times)):
            # userId, time, game, ra, password, name 
            #   0      1     2    3      4       5

            rank = RankPosition(i + 1, times[i][5], datetime.timedelta(seconds=times[i][1]))
            ranks.append(rank)

        return ranks

    def exibirRank():
        
        rank = generateRanks()

        # table = ttk.Treeview(root, style="Custom.Treeview")
        # table.grid(column=0, row=5)
        # table["columns"] = ("Posição", "RA", "Tempo")
        # table.column("RA", width=50)
        # table.column("Tempo", width=50)
        # table.column("Posição", width=50)
        # table.heading("#0", text="Posição")
        # table.heading("#1", text="RA")
        # table.heading("#2", text="Tempo")

        frame = Frame(root, width=500, height=500, bg=colors["background"])
        frame.place(anchor="center", relx=.5, rely=.5)

        text = ""
        for i in range(len(rank)):
            text += f"{rank[i].position}° - {rank[i].name} {rank[i].time}\n"
        # table.insert("", "end", values=(j,t))

        label = Label(frame, text= text, fg = '#3771A1', justify=CENTER, bg = colors["background"], font = ('Microsoft YaHei UI Light', 20), anchor='e')
        label.pack(side=TOP, pady=20)
        # label.place(anchor='e', relx=.5, rely=.5, y = 20, pady=20)

    # Definindo o estilo personalizado para a tabela
    style = ttk.Style()
    style.configure("Custom.Treeview",background="white",foreground="#3771A1",fieldbackground="#393E46")

    
    textofinalizar = Label(root,text="Jogo Finalizado!! :)", width=30, justify=CENTER, fg="#3771A1", bg=colors["background"], font=("Georgia",18), )
    textofinalizar.pack(padx=50, pady=25)

    botao = CTkButton(root, text="Visualizar Ranking", width=250, height=50, font=("Georgia",18), command=exibirRank, text_color="#fff", fg_color= "#3771A1", bg_color=colors["background"])
    botao.pack()

    root.mainloop()