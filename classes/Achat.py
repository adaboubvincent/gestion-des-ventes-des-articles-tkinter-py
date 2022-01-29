from classes import Article

class Achat(object):
    def __init__(self, numero: str, article: Article.Article, quantite: int, id: int=0):
        self.__numero = numero
        self.__article = article
        self.__quantite = quantite
        self.id = id
    
    def setNumero(self, numero: str):
        self.__numero = numero
    def setArticle(self, article: Article.Article):
        self.__article = article
    def setQuantite(self, quantite: int):
        self.__quantite = quantite

    def getNumero(self):
        return self.__numero
    def getArticle(self):
        return self.__article
    def getQuantite(self):
        return self.__quantite
    
    def modifierQuantite(self, quantite):
        self.setQuantite(quantite)
    
    def __str__(self):
        return "{} {} {}CFA {}Q".format(self.__numero, self.__article.getDesignation(), \
            self.__article.getPrix(), self.__quantite)