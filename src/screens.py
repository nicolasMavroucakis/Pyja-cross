from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from customtkinter import *
import datetime

import src.connection as connection
import src.game as game
import src.misc as misc

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
    user = CTkEntry(frame, width = 250, text_color = "white", border_width  = 0, bg_color=colors["background"], fg_color = colors["background"], font = ('Microsoft YaHei UI Light', 14), placeholder_text="RA")
    user.place(x =25, y = 80)

    Frame(frame, width = 295, height = 2, bg =colors["white"]).place(x = 25, y =107)

    senha = CTkEntry(frame,width = 250, bg_color=colors["background"], text_color = "white", fg_color = colors["background"], font = ('Microsoft YaHei UI Light', 14), show="*", border_width=0, placeholder_text="Senha")
    senha.place(x =25, y = 150)

    Frame(frame, width = 295, height = 2, bg =colors["white"]).place(x = 25, y =177)

    #Conexão da Tela de Login com o Banco de Dados
    def func_login():
        ra = user.get()
        senha_usuario = senha.get()

        if len(ra) == 10:
            loginResult = connection.login(ra, senha_usuario)
            if loginResult["auth"]:
                open_main_screen(loginResult, root)
            else:
                messagebox.showinfo("Erro","RA e/ou Senha inválidos")
        else:
            messagebox.showinfo("Erro", "RA inválido")

    #Criando botao de login e area para pessoas que nao possuem cadastro


    CTkButton(frame, width=270, height=40, text='Login',bg_color=colors["background"], fg_color=colors["theme"], corner_radius=5, text_color="white", command=func_login).place(x=35, y=204)
    # Button(frame, width =39, pady = 7, text = 'Login', bg = '#3771A1', fg = 'white', border = 0,command=func_login).place(x =35, y =204)
    label = Label(frame, text= "Não possui uma cadastro?", fg = colors["white"], bg = colors["background"], font = ('Microsoft YaHei UI Light', 10))
    label.place(x = 58, y = 270)

    sign_up = Button( master=frame, width = 0, text = 'Cadastre-se', border = 0, bg = colors["background"], cursor = 'hand2',fg = colors["theme"],font = ('Microsoft YaHei UI Light', 10),command=lambda: open_signin(root))
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

    CTkButton(root, width=300, height=100, font=('microsoft Yahei UILight',26, "bold"), text="PYTHON", fg_color=colors["theme"], text_color=colors["white"], corner_radius=10, command=lambda: open_game("python", root, 0)).place(x=150, y=350)
    CTkButton(root, width=300, height=100, font=('microsoft Yahei UILight',26, "bold"), text="JAVA", fg_color=colors["theme"], text_color=colors["white"], corner_radius=10, command=lambda: open_game("java", root, 1)).place(x=500,y=350)
    # Button(root, width=30, height=3, font=('microsoft Yahei UILight',15), text="PYTHON", bg="#3771A1", fg=colors["white"], border=0,command=lambda: open_game("python", root, 0)).place(x=150, y = 350)
    # Button(root, width=30, height=3, font=('microsoft Yahei UILight',15), text="JAVA", bg="#3771A1", fg=colors["white"], border=0, command=lambda: open_game("java", root, 1)).place(x=500, y=350)

    root.mainloop()

def open_main_screen(loginResult, window = None):

    if window:
        window.destroy()

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

    playButton = CTkButton(buttonsFrame, text="JOGAR", command=lambda: open_choose_screen(loginResult, root), width=300, height=70, fg_color="#3771A1", corner_radius=10, text_color="#fff", font = ('sans-serif', 23, 'bold'))
    playButton.place(x = 0, y = 60)

    rankButton = CTkButton(buttonsFrame, text="RANKING", command=lambda: open_ranking(root, loginResult), width=300, height=70, fg_color="#3771A1", corner_radius=10, text_color="#fff", font = ('sans-serif', 23, 'bold'))
    rankButton.place(x = 0, y = 170)

    img = ImageTk.PhotoImage(Image.open('images/_logo.png').resize((350, 350)))
    Label(root, image=img, bg="#2B2D2E").place(x=400,y=70)

    root.mainloop()

def open_ranking(window = None, loginResult = None):
    
    if window:
        window.destroy()

    root = Tk()
    root.geometry("925x500+300+200")
    root.iconbitmap("images/logo.ico")
    root.title("PyJa Cross")
    root.resizable(False, False)
    root.config(bg=colors['background'])

    def generateRanks(gameType):
        times = connection.getTimes(gameType)
        ranks = []

        flag = True

        for i in range(len(times)):
            # userId, time, game, ra, password, name 
            #   0      1     2    3      4       5

            if flag:
                color = "#414C55"
            else:
                color = "#313539"

            flag = not flag

            rank = misc.RankPosition(i + 1, times[i][5], datetime.timedelta(seconds=times[i][1]), color)
            ranks.append(rank)

        return ranks

    def exibirRank(gameType):

        rank = generateRanks(gameType)

        flag = True

        s = ttk.Style()
        s.theme_use("clam")

        s.map("Treeview", background=[('disabled','#000'), ('active','#fff')],foreground=[('disabled','#000')])
        s.configure("Treeview", rowheight=35, fieldbackground=colors["background"], borderwidth=0, font=("Arial",12))
        s.configure("Treeview.Heading", background=colors["theme"], borderwidth=0, font=("Arial",16), foreground="white")

        columns = ('position','name','time')

        tree = ttk.Treeview(root, columns=columns, show='headings', height=10, padding=2)

        tree.heading('position', text='POSIÇÃO')
        tree.heading('name', text='NOME')
        tree.heading('time', text='TEMPO')

        tree.column('position', anchor=CENTER, width=200)
        tree.column('name', anchor=CENTER, width=300)
        tree.column('time', anchor=CENTER, width=200)

        tree.bind('<Motion>', 'break')

        positions = []

        for i in range(len(rank)):

            positions.append((f'{rank[i].position}°', f'{rank[i].name}', f'{rank[i].time}'))

        for i in positions:

            if flag:
                tags = ("oddrow")
            else:
                tags = ("evenrow")

            flag = not flag
            tree.insert('', END, values=i, tags=tags)

        tree.tag_configure("oddrow",background="#414C55", foreground="white")
        tree.tag_configure("evenrow",background="#313539", foreground="white")

        tree.pack( anchor='c', pady=60)

    buttonsArea = Frame(root, width=500, height=30, bg=colors["background"])
    buttonsArea.place(x = 150, y = 10)

    typePython = CTkButton(buttonsArea, width=200, height=35, bg_color=colors["background"], fg_color=colors["theme"], text_color="white", text="PYTHON", command=lambda: exibirRank(0))
    typeJava = CTkButton(buttonsArea, width=200, height=35, bg_color=colors["background"], fg_color=colors["theme"], text_color="white", text="JAVA", command=lambda: exibirRank(1))
    returnButton = CTkButton(buttonsArea, width=200, height=35, text="TELA INICIAL", bg_color=colors["background"], fg_color=colors["theme"], text_color=colors["white"], command=lambda: open_main_screen(loginResult, root))

    typePython.pack(side=LEFT, padx=8, anchor='c')
    typeJava.pack(side=LEFT, padx=8, anchor='c')
    returnButton.pack(side=LEFT, padx=8, anchor='c')

    root.mainloop()