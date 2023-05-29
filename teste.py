from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk

def open_main_screen():
    root = Tk()
    root.iconbitmap("images/logo.ico")
    root.title("PyJa Cross")
    root.geometry("925x500+300+200")
    root.configure(bg = "#2B2D2E")
    root.resizable(False, False)

    ctk.set_appearance_mode("Dark")

    text = Label(root, text="Bem Vindo(a) ao PyJa Cross!", fg="#659FCF", bg="#2B2D2E", font = ('microsoft Yahei UILight', 23, 'bold'), justify=CENTER)
    text.place(x=250, y=20)

    buttonsFrame = Frame(root, width=300, height=350, bg="#2B2D2E")
    buttonsFrame.place(x = 10, y = 150)

    def play():
        print("JOGAR!")

    def rank():
        print("RANK!")

    playButton = ctk.CTkButton(buttonsFrame, text="JOGAR", command=play, width=300, height=70, fg_color="#3771A1", corner_radius=10, text_color="#fff", font = ('sans-serif', 23, 'bold'))
    playButton.place(x = 0, y = 60)

    rankButton = ctk.CTkButton(buttonsFrame, text="RANKING", command=rank, width=300, height=70, fg_color="#3771A1", corner_radius=10, text_color="#fff", font = ('sans-serif', 23, 'bold'))
    rankButton.place(x = 0, y = 170)

    img = ImageTk.PhotoImage(Image.open('images/_logo.png').resize((350, 350)))
    Label(root, image=img, bg="#2B2D2E").place(x=400,y=70)

    root.mainloop()

open_main_screen()