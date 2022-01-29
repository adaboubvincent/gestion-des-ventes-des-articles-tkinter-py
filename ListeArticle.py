import tkinter as tk
from tkinter import ttk
from AjouterArticle import AjouterArticle

class ListeArticle(tk.Frame):  

    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width = 1000, height = 900, bg = "black", **kwargs)
        self.grid(stick = "s",)


        self.bienvenu = tk.Label(fenetre, text="Liste articles",
                            padx = 2, pady = 2, bd = 8,fg = "white", bg = "black",
                            font = ("arial", 50, "bold"))
        self.bienvenu.place(x=60,y=20)

        tableau = ttk.Treeview(fenetre, columns=('code', 'designation', 'prix', 'categorie'))

        tableau.heading('code', text='Code')
        tableau.heading('designation', text='Désignation')
        tableau.heading('prix', text='Prix')
        tableau.heading('categorie', text='Catégorie')

        tableau['show'] = 'headings'

        tableau.column("code", anchor="center")
        tableau.column("designation", anchor="center")
        tableau.column("prix", anchor="center")
        tableau.column("categorie", anchor="center")

        tableau.place(x=10,y=100)

        count = 0
        for article in AjouterArticle.liste_articles:
            tableau.insert('', 'end',iid=count, text=f'{count + 1}', values=(article.getCode(), article.getDesignation(),\
                article.getPrix(), article.getCategorie()))
            count+=1
        if not AjouterArticle.liste_articles:
            self.bienvenu.configure(text = "Auncun article n'a été enrégistré")
            tableau.pack_forget()




    def destroy_frame(self):
        self.destroy()