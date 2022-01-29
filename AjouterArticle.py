import tkinter as tk
from tkinter import ttk
from classes import Article
from tkinter import messagebox
import sqlite3

from Accueil import Accueil

class AjouterArticle(tk.Frame):  
    #Attribut static  
    con = sqlite3.connect(Accueil.DB_NAME)
    cur = con.cursor()
    cur.execute('''SELECT id, code, designation, prix, categorie FROM article''')
    resultat = cur.fetchall()
    con.close()                                                            
    liste_articles = [Article.Article(enreg[1], enreg[2],int(enreg[3]),enreg[4], enreg[0]) for enreg in resultat]

    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width = 1000, height = 900, bg = "black", **kwargs)
        self.grid(stick = "s",)


        self.bienvenu = tk.Label(fenetre, text="Ajouter article",
                            padx = 2, pady = 2, bd = 8,fg = "white", bg = "black",
                            font = ("arial", 50, "bold"))
        self.bienvenu.place(x=60,y=20)



        #tk.Label(fenetre, text="Ajouter article", font=('Arial', 20)).pack(padx=1, pady=1)

        #Etiquette et le champ du code
        ttk.Label(fenetre, text='Code : ',
            font = ("arial", 20, "bold")).place(x=50, y=120)
        self.code_var = tk.StringVar()
        self.code_entry = ttk.Entry(fenetre, font = ("arial", 20, "bold"),
            textvariable=self.code_var)
        self.code_entry.place(x=350,y=120)

        #Etiquette et le champ du designation
        ttk.Label(fenetre, text='Désignation : ',
            font = ("arial", 20, "bold")).place(x=50, y=180)
        self.designation_var = tk.StringVar()
        self.designation_entry = ttk.Entry(fenetre, font = ("arial", 20, "bold"),
            textvariable=self.designation_var)
        self.designation_entry.place(x=350,y=180)

        #Etiquette et le champ du prix
        ttk.Label(fenetre, text='Prix : ',
            font = ("arial", 20, "bold")).place(x=50, y=240)
        self.prix_var = tk.StringVar()
        self.prix_entry = ttk.Entry(fenetre, font = ("arial", 20, "bold"),
            textvariable=self.prix_var)
        self.prix_entry.place(x=350,y=240)

        #Etiquette et le champ du categorie
        ttk.Label(fenetre, text='Catégorie : ',
            font = ("arial", 20, "bold")).place(x=50, y=300)
        self.categorie_var = tk.StringVar()
        self.categorie_entry = ttk.Entry(fenetre, font = ("arial", 20, "bold"),
            textvariable=self.categorie_var)
        self.categorie_entry.place(x=350,y=300)

        ttk.Button(fenetre, text="Ajouter article", padding = 10, command=lambda:self.ajouter(\
            self.code_var.get(), self.designation_var.get(), self.prix_var.get(), \
                self.categorie_var.get())).place(x=270, y=380)



    def ajouter(self, code:str, designation: str, prix: float, categorie: str):
        if prix.isdigit():

            AjouterArticle.liste_articles.append(
                Article.Article(code, designation, eval(prix), categorie)
            )
            con = sqlite3.connect(Accueil.DB_NAME)
            cur = con.cursor()

            values = (code, designation, int(prix), categorie)
            cur.execute('''INSERT INTO article(code, designation, prix, categorie) VALUES(?,?,?,?)
                    ''', values)
            con.commit()
            con.close()


        
            messagebox.showinfo("Infos", "Article a été ajouté avec succès")
            self.code_var.set("")
            self.categorie_var.set("")
            self.prix_var.set("")
            self.designation_var.set("")
        else:
            messagebox.showwarning("warning", "Le prix doit être un nombre entier(CFA)")



    def destroy_frame(self):
        self.destroy()