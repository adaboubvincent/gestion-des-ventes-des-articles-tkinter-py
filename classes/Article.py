class Article(object):
    def __init__(self, code: str, designation: str, prix: float, categorie: str, id: int=0):
        self.__code = code
        self.__designation = designation
        self.__prix = prix
        self.__categorie = categorie
        self.id = id

    def setCode(self, code: str):
        self.__code = code
    def setDesignation(self, designation: str):
        self.__designation = designation
    def setPrix(self, prix: float):
        self.__prix = prix
    def setCategorie(self, categorie: str):
        self.__categorie = categorie

    def getCode(self):
        return self.__code
    def getDesignation(self):
        return self.__designation
    def getPrix(self):
        return self.__prix
    def getCategorie(self):
        return self.__categorie

    def affiche(self):

        print("Code : {}\nDesignation : {}\nPrix : {}\nCategorie : {}".format(\
            self.__code, self.__designation, self.__prix, self.__categorie))
        print("=====================================================================")
    
    def comparer(self, article1: object, article2: object):
        if article1.getCode() == article2.getCode() and article1.getDesignation() == article2.getDesignation() and article1.getPrix() == article2.getPrix() and article1.getCategorie() == article2.getCategorie():
            print("Les deux articles sont les mêmes")
            return True
        print("Les deux articles sont différents")
        return False

    def __str__(self):
        return "{} {} {}CFA {}".format(self.__code, self.__designation, self.__prix, self.__categorie)