import tkinter as tk
from tkinter import ttk
from AjouterFacture import AjouterFacture
import sqlite3
from classes import Facture
from classes import Achat
from classes import Article
from Accueil import Accueil

class ListeFacture(tk.Frame):  
    
    def __init__(self, fenetre, **kwargs):
        con = sqlite3.connect(Accueil.DB_NAME)
        cur = con.cursor()
        cur.execute('''SELECT id, numero, date_facture FROM facture''')
        resultat = cur.fetchall()
        con.close()
        liste_factures = [Facture.Facture(enreg[1], enreg[2], [], enreg[0]) for enreg in resultat]
        for coun in range(len(liste_factures)):
            con = sqlite3.connect(Accueil.DB_NAME)
            cur = con.cursor()
            cur.execute('''SELECT id, numero, article_id, quantite FROM achat WHERE facture_id=?''', (liste_factures[coun].id, ))
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
            liste_factures[coun].setAchats(liste_achats)



        tk.Frame.__init__(self, fenetre, width = 1000, height = 900, bg = "black", **kwargs)
        self.grid(stick = "s",)


        self.bienvenu = tk.Label(fenetre, text="Liste Ventes",
                            padx = 2, pady = 2, bd = 8,fg = "white", bg = "black",
                            font = ("arial", 50, "bold"))
        self.bienvenu.place(x=60,y=20)

        tableau = ttk.Treeview(fenetre, columns=('numero', 'date', 'achats', 'montant'))

        tableau.heading('numero', text='Numéro')
        tableau.heading('date', text='Date')
        tableau.heading('achats', text='Achats')
        tableau.heading('montant', text='Montant à payé')

        tableau['show'] = 'headings'

        tableau.column("numero", anchor="center")
        tableau.column("date", anchor="center")
        tableau.column("achats", anchor="center")
        tableau.column("montant", anchor="center")

        tableau.place(x=10,y=100)

        count = 0
        for facture in liste_factures:
            tableau.insert('', 'end',iid=count, text=f'{count + 1}', values=(facture.getNumero(), facture.getDate(),\
                facture.getAchats(), facture.montantTotalFacture()))
            count+=1
        if not liste_factures:
            self.bienvenu.configure(text = "Auncune vente n'a été enrégistrée")
            tableau.pack_forget()




    def destroy_frame(self):
        self.destroy()

        #Deo Gratias