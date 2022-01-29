import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from AjouterArticle import AjouterArticle
from classes import Achat
from classes import Article
import sqlite3

from Accueil import Accueil


class AjouterAchat(tk.Frame):  
    #Attribut static  
    con = sqlite3.connect(Accueil.DB_NAME)
    cur = con.cursor()
    cur.execute('''SELECT id, numero, article_id, quantite FROM achat''')
    resultat = cur.fetchall()
    con.close()
    liste_achats = [Achat.Achat(enreg[1], enreg[2],int(enreg[3]), enreg[0]) for enreg in resultat]

    for i in range(len(liste_achats)):
        con = sqlite3.connect(Accueil.DB_NAME)
        cur = con.cursor()
        cur.execute('''SELECT code, designation, prix, categorie  FROM article WHERE id=?''', (liste_achats[i].getArticle(),))
        obj = cur.fetchone()
        con.close()
        art = obj
        liste_achats[i].setArticle(Article.Article(art[0], art[1],int(art[2]),art[3], liste_achats[i].getArticle()))
    
    
    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width = 1000, height = 900, bg = "black", **kwargs)
        self.grid(stick = "s",)


        self.bienvenu = tk.Label(fenetre, text="Ajouter Achat",
                            padx = 2, pady = 2, bd = 8,fg = "white", bg = "black",
                            font = ("arial", 50, "bold"))
        self.bienvenu.place(x=60,y=20)



        #tk.Label(fenetre, text="Ajouter article", font=('Arial', 20)).pack(padx=1, pady=1)

        #Etiquette et le champ du numero
        ttk.Label(fenetre, text='Numéro : ',
            font = ("arial", 20, "bold")).place(x=50, y=120)
        self.numero_var = tk.StringVar()
        self.numero_entry = ttk.Entry(fenetre, font = ("arial", 20, "bold"),
            textvariable=self.numero_var)
        self.numero_entry.place(x=350,y=120)

        #Etiquette et le champ du article
        con = sqlite3.connect(Accueil.DB_NAME)
        cur = con.cursor()
        cur.execute('''SELECT id, code, designation, prix, categorie FROM article''')
        resultat = cur.fetchall()
        con.close()                                                            
        AjouterArticle.liste_articles = [Article.Article(enreg[1], enreg[2],int(enreg[3]),enreg[4], enreg[0]) for enreg in resultat]

        ttk.Label(fenetre, text='Article : ',
            font = ("arial", 20, "bold")).place(x=50, y=180)
        self.article_entry = ttk.Combobox(fenetre, font = ("arial", 20, "bold"),
            values=AjouterArticle.liste_articles)
        self.article_entry.place(x=350,y=180)

        #Etiquette et le champ du quantite
        ttk.Label(fenetre, text='Quantité : ',
            font = ("arial", 20, "bold")).place(x=50, y=240)
        self.quantite_var = tk.StringVar()
        self.quantite_entry = ttk.Entry(fenetre, font = ("arial", 20, "bold"),
            textvariable=self.quantite_var)
        self.quantite_entry.place(x=350,y=240)

        ttk.Button(fenetre, text="Ajouter achat", padding = 10, command=lambda:self.ajouter(\
            self.numero_var.get(), self.article_entry.get(), self.quantite_var.get())).place(x=270, y=320)



    def ajouter(self, numero:str, article: str, quantite: int):
        if quantite.isdigit():
            art = [elt for elt in AjouterArticle.liste_articles if elt.__str__() == article][0]
            AjouterAchat.liste_achats.append(
                Achat.Achat(numero, art, int(quantite))
            )

            con = sqlite3.connect(Accueil.DB_NAME)
            cur = con.cursor()

            values = (numero, art.id, int(quantite), None)
            cur.execute('''INSERT INTO achat(numero, article_id, quantite, facture_id) VALUES(?,?,?,?)
                    ''', values)
            con.commit()
            con.close()


            messagebox.showinfo("Infos", "Achat a été ajouté avec succès")
            self.numero_var.set("")
            self.quantite_var.set("")
            self.article_entry.set("")
        else:
            messagebox.showwarning("warning", "La quantité doit être un entier")


    def destroy_frame(self):
        self.destroy()