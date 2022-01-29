import datetime, time
from classes import Achat

class Facture(object):
    def __init__(self, numero: str, date: str = None, achats: list = [], id: int=0):
        self.__numero = numero
        '''if date == None:
            date_now = time.localtime()
            date_now2 = ("{}/{}/{}".format(date_now[2],date_now[1],date_now[0])).split("/")
            self.__date = datetime.date(int(date_now2[2]), int(date_now2[1]), int(date_now2[0]))
        else:
            self.__date = date'''
        self.id = id
        self.setDate(date)
        
        self.__achats = achats

    def setNumero(self, numero: str):
        self.__numero = numero
    def setAchats(self, achats: str):
        self.__achats = achats
        
    def setDate(self, date):
        if date == None:
            date_now = time.localtime()
            date_now2 = ("{}/{}/{}".format(date_now[2],date_now[1],date_now[0])).split("/")
            self.__date = datetime.date(int(date_now2[2]), int(date_now2[1]), int(date_now2[0]))
        else:
            self.__date = date
    
    def getNumero(self):
        return self.__numero
    def getDate(self):
        return self.__date
    def getAchats(self):
        return self.__achats

    def ajouterAchat(self, achat: Achat.Achat):
        existe = False
        for elt in self.__achats:
            if achat.getNumero() == elt.getNumero():
                print("Achat existe déjà !")
                existe = True
        if not existe:
            self.__achats.append(achat)

    def montantTotalFacture(self):
        montant_total: float = 0
        for elt in self.__achats:
            montant_total += elt.getArticle().getPrix() * elt.getQuantite()

        return montant_total
    
    def detailsFacture(self):
        print("\t\t\t\tNuméro facture : {} ; date facture : {}".format(self.__numero, self.__date))
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tListe des Achats")
        print("Désignation\t\t\t\tRemise\t\t\t\tprix(en DH)\t\t\t\tQuantite\t\t\t\tPrix Total")
        for elt in  self.__achats:
            print("{}\t\t\t{}\t\t\t\t\t\t\t\t{}\t\t\t\t\t\t{}\t\t\t\t\t\t\t\t{}".format(elt.getArticle().getDesignation(), \
                0, elt.getArticle().getPrix(), \
                elt.getQuantite(), elt.getArticle().getPrix() * elt.getQuantite()))

        print("Montant de la facture : ", self.montantTotalFacture())