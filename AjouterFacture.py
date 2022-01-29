from install import install
try:
    from tkcalendar import DateEntry
except Exception as exc:
    install("tkcalendar")
    from tkcalendar import DateEntry


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from AjouterAchat import AjouterAchat
from classes import Facture
from classes import Achat
from classes import Article
import sqlite3

from Accueil import Accueil

class AjouterFacture(tk.Frame):  
    #Attribut static                                                                     
    liste_factures = []

    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, width = 1000, height = 900, bg = "black", **kwargs)
        self.grid(stick = "s",)


        self.bienvenu = tk.Label(fenetre, text="Ajouter facture",
                            padx = 2, pady = 2, bd = 8,fg = "white", bg = "black",
                            font = ("arial", 50, "bold"))
        self.bienvenu.place(x=60,y=20)


        #Etiquette et le champ du numero
        ttk.Label(fenetre, text='Numéro : ',
            font = ("arial", 20, "bold")).place(x=50, y=120)
        self.numero_var = tk.StringVar()
        self.numero_entry = ttk.Entry(fenetre, font = ("arial", 20, "bold"),
            textvariable=self.numero_var)
        self.numero_entry.place(x=350,y=120)
        #Etiquette et le champ du date
        ttk.Label(fenetre, text='Date : ',
            font = ("arial", 20, "bold")).place(x=50, y=180)
        #self.date_var = tk.StringVar()
        """ self.date_entry = ttk.Entry(fenetre, font = ("arial", 20, "bold"),
            textvariable=self.date_var) """
        self.date_entry = DateEntry(fenetre, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
        self.date_entry.place(x=350,y=180)

        #Etiquette et le champ du achat
        self.yscrollbar = tk.Scrollbar(fenetre)
        self.yscrollbar.place(x=350,y=240)
        self._list = tk.Listbox(fenetre, selectmode = "multiple", 
               yscrollcommand = self.yscrollbar.set)
        self._list.place(x=350,y=240)
        ttk.Label(fenetre, text='Liste Achats : ',
            font = ("arial", 20, "bold")).place(x=50, y=240)
        

        con = sqlite3.connect(Accueil.DB_NAME)
        cur = con.cursor()
        cur.execute('''SELECT id, numero, article_id, quantite, facture_id FROM achat''')
        resultat = cur.fetchall()
        con.close()
        AjouterAchat.liste_achats = [Achat.Achat(enreg[1], enreg[2],int(enreg[3]), enreg[0]) for enreg in resultat if not bool(enreg[4])]

        for i in range(len(AjouterAchat.liste_achats)):
            con = sqlite3.connect(Accueil.DB_NAME)
            cur = con.cursor()
            cur.execute('''SELECT code, designation, prix, categorie  FROM article WHERE id=?''', \
                (AjouterAchat.liste_achats[i].getArticle(),))
            obj = cur.fetchone()
            con.close()
            art = obj
            AjouterAchat.liste_achats[i].setArticle(Article.Article(art[0], art[1],int(art[2]),art[3], \
                AjouterAchat.liste_achats[i].getArticle()))
        
        

        for each_item in range(len(AjouterAchat.liste_achats)):
            self._list.insert(tk.END, AjouterAchat.liste_achats[each_item])
            self._list.itemconfig(each_item, bg = "lime")
        self.yscrollbar.config(command = self._list.yview)

        ttk.Button(fenetre, text="Ajouter achat", padding = 10, command=lambda:self.ajouter(\
            self.numero_var.get(), self.date_entry.get_date(), [self._list.get(i) for i in self._list.curselection() ])).place(x=270, y=450)



    def ajouter(self, numero:str, _date: str, achats: int):
        achats_l = [elt for elt in AjouterAchat.liste_achats for achat in achats if elt.__str__() == achat]
        AjouterFacture.liste_factures.append(
            Facture.Facture(numero, _date, achats_l)
        )

        con = sqlite3.connect(Accueil.DB_NAME)
        cur = con.cursor()

        values = (numero, _date)
        cur.execute('''INSERT INTO facture(numero, date_facture) VALUES(?,?)
                ''', values)
        con.commit()
        con.close()

        con = sqlite3.connect(Accueil.DB_NAME)
        cur = con.cursor()
        cur.execute('''SELECT id  FROM facture WHERE numero=? AND date_facture=?''', (numero,_date))
        obj = cur.fetchone()
        con.close()
        _id = obj[0] #id de la facture enrégistrée actuellemnt


        con = sqlite3.connect(Accueil.DB_NAME)
        cur = con.cursor()
        for ach in achats_l:
            cur.execute('''UPDATE achat SET facture_id=? WHERE id=?''', (_id, ach.id))
        con.commit()
        con.close()

        messagebox.showinfo("Infos", "Facture a été ajoutée avec succès")
        self.numero_var.set("")

        con = sqlite3.connect(Accueil.DB_NAME)
        cur = con.cursor()
        cur.execute('''SELECT id, numero, article_id, quantite, facture_id FROM achat''')
        resultat = cur.fetchall()
        con.close()
        AjouterAchat.liste_achats = [Achat.Achat(enreg[1], enreg[2],int(enreg[3]), enreg[0]) for enreg in resultat if not bool(enreg[4])]

        for i in range(len(AjouterAchat.liste_achats)):
            con = sqlite3.connect(Accueil.DB_NAME)
            cur = con.cursor()
            cur.execute('''SELECT code, designation, prix, categorie  FROM article WHERE id=?''', \
                (AjouterAchat.liste_achats[i].getArticle(),))
            obj = cur.fetchone()
            con.close()
            art = obj
            AjouterAchat.liste_achats[i].setArticle(Article.Article(art[0], art[1],int(art[2]),art[3], \
                AjouterAchat.liste_achats[i].getArticle()))

        self._list.delete(0,'end')
        for each_item in range(len(AjouterAchat.liste_achats)):
            self._list.insert(tk.END, AjouterAchat.liste_achats[each_item])
            self._list.itemconfig(each_item, bg = "lime")



    def destroy_frame(self):
        self.destroy()