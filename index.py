#Importation de tkinter avec ttk module
from install import install
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
try:
    import sqlite3
except Exception as exc:
    install("pysqlite3")
    import sqlite3

from Accueil import Accueil #Importer la classe Accueil dans Accueil


def connexionDB():
    #SQLite3 instancié
    con = sqlite3.connect(Accueil.DB_NAME)
    cur = con.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS article
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,code text, designation text, prix float, categorie text);
        ''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS facture
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,numero text, date_facture text);
        ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS achat
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,numero text, article_id INTEGER, quantite INTEGER, facture_id INTEGER null, 
        FOREIGN KEY(facture_id) REFERENCES facture(id));
        ''')

    con.commit()
    con.close()

if __name__ == '__main__':
    connexionDB()



from AjouterArticle import AjouterArticle #Importer la classe AjouterArticle dans AjouterArticle
from ListeArticle import ListeArticle #Importer la classe ListeArticle dans ListeArticle
from AjouterAchat import AjouterAchat #Importer la classe AjouterAchat dans AjouterAchat
from ListeAchat import ListeAchat #Importer la classe ListeAchat dans ListeAchat
from AjouterFacture import AjouterFacture #Importer la classe AjouterFacture dans AjouterFacture
from ListeFacture import ListeFacture #Importer la classe ListeFacture dans ListeFacture







fenetre = tk.Tk()   #Créeation de la fenetre
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()  #Réccupération de la largeur et la hauteur de l'écran
fenetre.geometry("%dx%d+%d+%d" %(750,580,(fenetre.winfo_screenwidth()-750)/2,(fenetre.winfo_screenheight()-580)/2)) #Rédimentionnement de la fenetre
fenetre.minsize(750,580) #Figer la largeur et la hauteur minimales de la fenetre
fenetre.config(bg="black") #La couleur de la fenetre
fenetre.title("Gestion de Vente") #Le titre de la fenetre

ajouterArticle = None
accueil = None
listeArticle = None
ajouterAchat = None
listeAchat = None
ajouterFacture = None
listeFacture = None

def accueil_action():
    global accueil
    destroy_all_frame()
    accueil = Accueil(fenetre)
    

def ajouter_article_action():
    global ajouterArticle
    destroy_all_frame()
    ajouterArticle = AjouterArticle(fenetre)

def liste_article_action():
    global listeArticle
    destroy_all_frame()
    listeArticle = ListeArticle(fenetre)

def ajouter_article_achat():
    global ajouterAchat
    destroy_all_frame()
    ajouterAchat = AjouterAchat(fenetre)

def liste_achat_action():
    global listeAchat
    destroy_all_frame()
    listeAchat = ListeAchat(fenetre)

def ajouter_facture_achat():
    global ajouterFacture
    destroy_all_frame()
    ajouterFacture = AjouterFacture(fenetre)
def liste_facture_action():
    global listeFacture
    destroy_all_frame()
    listeFacture = ListeFacture(fenetre)

def destroy_all_frame():
    """ Fonction permettant de détruire tous les frames(Components) """
    global accueil, ajouterArticle, listeArticle, ajouterAchat, listeAchat, ajouterFacture
    if accueil: accueil.destroy_frame()
    if ajouterArticle: ajouterArticle.destroy_frame()
    if listeArticle: listeArticle.destroy_frame()
    if ajouterAchat: ajouterAchat.destroy_frame()
    if listeAchat: listeAchat.destroy_frame()
    if ajouterFacture: ajouterFacture.destroy_frame()
    if listeFacture: listeFacture.destroy_frame()


accueil_action() #Ouverture du component(frame) accueil



#Menu bar config
menubar = tk.Menu(fenetre)

menuArticle = tk.Menu(menubar)
menuArticle.add_command(label="Ajouter Article", command=ajouter_article_action)
menuArticle.add_command(label="Liste des Articles", command=liste_article_action)
menubar.add_cascade(label="Gestion des Articles", menu=menuArticle)


menuAchat = tk.Menu(menubar)
menuAchat.add_command(label="Enrégistrer Achat", command=ajouter_article_achat)
menuAchat.add_command(label="Liste des Achats", command=liste_achat_action) 
menubar.add_cascade(label="Gestion des Achats", menu=menuAchat)

menuVente = tk.Menu(menubar)
menuVente.add_command(label="Enrégistrer Vente", command=ajouter_facture_achat)
menuVente.add_command(label="Liste des Ventes", command=liste_facture_action) 
menubar.add_cascade(label="Gestion des Ventes", menu=menuVente)


import sys
autre = tk.Menu(menubar)
autre.add_command(label="Accueil", command=accueil_action)
autre.add_command(label="Sortir", command=sys.exit)
menubar.add_cascade(label="Autre", menu=autre)

fenetre.config(menu=menubar)




fenetre.mainloop() #Bouclage sur la fenetre

