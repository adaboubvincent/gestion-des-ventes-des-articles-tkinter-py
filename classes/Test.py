from classes import (
        Article, Achat, Facture
    )

#nstanciez deux nouveaux articles
article1 = Article.Article("Chaussure Sport", "désignation001", 5000, "Chaussure")
article2 = Article.Article("Banane", "désignation002", 1000, "Fruit")

#Affichez les informations de l’article
article1.affiche()
article2.affiche()

#Créez aussi deux achats correspondants aux deux articles instanciés
achat1 = Achat.Achat("ACHATCHAUSSURE0001", article1, 10)
achat2 = Achat.Achat("ACHATBANANE0001", article2, 7)

#Modifiez la quantité d’articles achetés pour le premier achat
achat1.modifierQuantite(11)

#Créez ensuite une nouvelle facture correspondant à une nouvelle vente
facture1 = Facture.Facture("FACTURE001")

#Ajoutez ensuite les deux achats précédents à la facture
facture1.ajouterAchat(achat1)
facture1.ajouterAchat(achat2)

#Affichez le montant total de la facture
print("Le montant total de la facture : ",facture1.montantTotalFacture())

#Affichez tous les détails de la facture
print("\n================================================================")
facture1.detailsFacture()