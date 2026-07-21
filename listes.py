#listes
livres = ["Things Fall Apart", "Une si longue lettre", "Les bouts de bois de Dieu"]
auteurs = ["Chinua Achebe", "Mariama Bâ", "Sembène Ousmane"]

#Afficher le premier élément de la liste
print(livres[0])
#Afficher le deuxième élément de la liste
print(livres[1])
#Afficher le troisième élément de la liste
print(livres[2])
print("---------------------------------------------------")

# Afficher toute la liste avec une boucle for
for livre in livres:
    print(livre)
print("----------------------------------------------------")

#Afficher chaque livre avec son auteur
for i in range(len(livres)):
    print(f"{livres[i]} est écrit par : {auteurs[i]}")
print("----------------------------------------------------")

#Les fonctions
# noinspection PyShadowingNames
def afficher_livres(liste_livres):
    for livre in liste_livres:
        print(livre)

#Appelle de la fonction pour afficher les livres
afficher_livres(livres)
print("----------------------------------------------------")

#Appelle de la fonction pour afficher les auteurs
afficher_livres(auteurs)
print("----------------------------------------------------")

#fonction pour afficher livre_auteur
# noinspection PyShadowingNames
def afficher_livre_auteur(liste_livres, liste_auteurs):
    for i in range(len(liste_livres)):
        print(f"{liste_livres[i]} est écrit par : {liste_auteurs[i]}")

#Appelle de la fonction pour afficher les livres avec leurs auteurs
afficher_livre_auteur(livres, auteurs)
print("----------------------------------------------------")

#fonction pour compter les livres dans la liste
def compter_livres(liste_livres):
    return len(liste_livres)

total = compter_livres(livres)
print(f"La bibliothèque contient {total} livres.")