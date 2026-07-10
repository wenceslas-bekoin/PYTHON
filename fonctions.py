#fonction dire bonjour
def dire_bonjour():
    print("Bonjour! Je vous salue depuis la fonction dire_bonjour() dans le fichier fonctions.py.")

# Appel de la fonction dire_bonjour()
dire_bonjour()

print("\n")  # Ajout d'une ligne vide pour séparer les sorties

# Fonction avec un paramètre
def dire_bonjour_a(nom):
    print(f"Bonjour, {nom}! Je vous salue depuis la fonction dire_bonjour_a() dans le fichier fonctions.py.")

# Appel de la fonction dire_bonjour_a()avec argument
dire_bonjour_a("Trésor")
dire_bonjour_a("Vital")
dire_bonjour_a("Béatrice")

print("\n")

# Fonction avec paramtrès par défaut
def ma_vision(but="Je souhaite devenir un développeur python compétent et un homme très sage."):
    print(f"Ma vision est : {but}")

# Appel de la fonction ma_vision()
ma_vision()

print("\n")

#  créer une calculatrice simple (utilisation de return)
def calculer_aire_rectangle(longueur, largeur):
    """Calculer l'aire d'un rectangle"""
    aire = longueur * largeur
    return aire

# Vérifier qu'un nombre est paire
def est_pair(nombre):
    """Vérifier si un nombre est paire"""
    if nombre % 2 == 0:
        return True
    else:
        return False
    
# calculer l'aire d'un rectangle
print(calculer_aire_rectangle(4, 5))

# vérifier si un nombre sest paire
print(est_pair(5))
print(est_pair(20))