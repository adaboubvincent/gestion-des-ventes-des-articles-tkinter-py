import tkinter as tk
from tkinter import ttk
from AjouterAchat import AjouterAchat

class ListeAchat(tk.Frame):  

    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width = 1000, height = 900, bg = "black", **kwargs)
        self.grid(stick = "s",)


        self.bienvenu = tk.Label(fenetre, text="Liste achats",
                            padx = 2, pady = 2, bd = 8,fg = "white", bg = "black",
                            font = ("arial", 50, "bold"))
        self.bienvenu.place(x=60,y=20)

        tableau = ttk.Treeview(fenetre, columns=('numero', 'article', 'quantite'))

        tableau.heading('numero', text='Numéro')
        tableau.heading('article', text='Article')
        tableau.heading('quantite', text='Quantite')

        tableau['show'] = 'headings'

        tableau.column("numero", anchor="center")
        tableau.column("article", anchor="center")
        tableau.column("quantite", anchor="center")

        tableau.place(x=10,y=100)

        count = 0
        for achat in AjouterAchat.liste_achats:
            tableau.insert('', 'end',iid=count, text=f'{count + 1}', values=(achat.getNumero(), achat.getArticle(),\
                achat.getQuantite()))
            count+=1
        if not AjouterAchat.liste_achats:
            self.bienvenu.configure(text = "Auncun achat n'a été enrégistré")
            tableau.pack_forget()




    def destroy_frame(self):
        self.destroy()