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

# Parcourrire toute la liste avec une boucle for
for livre in livres:
    print(livre)

print("----------------------------------------------------")

#Afficher chaque livre avec son auteur
for i in range(len(livres)):
    print(f"{livres[i]} est écrit par : {auteurs[i]}")

print("----------------------------------------------------")

#Les fonctions
def afficher_livres(listes):
    for livre in listes:
        print(livre)

#Appelle de la fonction pour afficher les livres
afficher_livres(livres)

print("----------------------------------------------------")
#Appelle de la fonction pour afficher les auteurs
afficher_livres(auteurs)

print("----------------------------------------------------")

#fonction pour afficher livre_auteur
def afficher_livre_auteur(livres, auteurs):
    for i in range(len(livres)):
        print(f"{livres[i]} est écrit par : {auteurs[i]}")

#Appelle de la fonctoin pour afficher les livres avec leurs auteurs
afficher_livre_auteur(livres, auteurs)

print("----------------------------------------------------")

#fonction pour compter les livres dans la liste
def compter_livres(livres):
    return len(livres)
total = compter_livres(livres)
print(f"La bibliothèque contient {total} livres.")

