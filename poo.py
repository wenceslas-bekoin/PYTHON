#création de la classe Livre
class Livre:
    def __init__(self, titre, auteur, pages):
        self.titre = titre
        self.auteur = auteur
        self.pages = pages

#Les méthodes
    def afficher(self):
        print(f"{self.titre} est écrit par {self.auteur.nom} et contient {self.pages} pages.")

# création de la classe auteur

class Auteur:
    def __init__(self, nom, nationalite, date_naissance):
        self.nom = nom
        self.nationalite = nationalite
        self.date_naissance = date_naissance

# création de la méthode afficher pour la classe Auteur
    def afficher(self):
        print(f"{self.nom} est {self.nationalite} et est né(e) le {self.date_naissance} .")

#création de l'objet auteur1
auteur1 = Auteur("Chinua Achebe", "Nigérian", "16 novembre 1930")

#création de l'objet auteur2
auteur2 = Auteur("Mariama Bâ", "Sénégalaise", "17 avril 1920")

#création de l'objet auteur3
auteur3 = Auteur("Sembène Ousmane", "Sénégalaise", "1er janvier 1923")


#Création de l'objet livre1
livre1 = Livre("Things Fall Apart", auteur1, 209)
#objet livre2
livre2 = Livre("Une si longue lettre", auteur2, 152)
#objet livre3
livre3 = Livre("Les bouts de bois de Dieu", auteur3, 256)

#Afficher titre, auteur et nombre de pages du livre1
print(f"{livre1.titre} est écrit par {livre1.auteur.nom} et contient {livre1.pages} pages.")
#Afficher titre, auteur et le nombre de pages du livre2
print(f"{livre2.titre} est écrit par {livre2.auteur.nom} et contient {livre2.pages} pages.")
#Afficher titre, auteur et le nombre de pages du livre3
print(f"{livre3.titre} est écrit par {livre3.auteur.nom} et contient {livre3.pages} pages.")

#Afficher des livres, auteurs et le nombres de pages avec la boucle for
for livre in [livre1, livre2, livre3]:
    print(f"{livre.titre} est écrit par {livre.auteur.nom} et contient {livre.pages} pages.")

print("----------------------------------------------------")

#Appelle méthode pour afficher les livres, les auteurs et le nombre de pages avec for
for livre in [livre1, livre2, livre3]:
    livre.afficher()

print("----------------------------------------------------")

#Appelle de la méthode afficher pour les auteurs avec for

for auteur in [auteur1, auteur2, auteur3]:
    auteur.afficher()
