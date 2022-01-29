from tkinter import *
from tkinter import ttk

class Accueil(Frame):                                                                       
    DB_NAME: str = 'gestion_vente.db'
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width = 1000, height = 900, bg = "black", **kwargs)
        self.grid(stick = "s",)

        self.bienvenu = Label(fenetre, text="Bienvenu sur l'application de gestion de vente",
                            padx = 2, pady = 2, bd = 8,fg = "white", bg = "black",
                            font = ("arial", 20, "bold"))
        self.bienvenu.place(x=50,y=50)

    def destroy_frame(self):
        self.destroy()