import psycopg2

# 1️ Connexion
connexion = psycopg2.connect(
    host     = "localhost",
    database = "bibliothèque",
    user     = "bekoin",
    password = "wen@ce$l&2026"
)
curseur = connexion.cursor()

# 2️Fonctions
def get_livres():
    """Récupérer tous les livres"""
    curseur.execute("SELECT titre, genre FROM livres")
    return curseur.fetchall()

def ajouter_livre(titre, id_auteur, date_publication, genre):
    """Ajouter un livre"""
    curseur.execute(
        "INSERT INTO livres(titre, id_auteur, date_publication, genre) VALUES(%s, %s, %s, %s)",
        (titre, id_auteur, date_publication, genre)
    )
    connexion.commit()

def get_auteurs():
    """Récupérer tous les auteurs"""
    curseur.execute("SELECT nom, prenom, nationalite FROM auteurs")
    return curseur.fetchall()

def ajouter_auteur(nom, prenom, nationalite):
    """Ajouter un auteur"""
    curseur.execute(
        "ISERT INTO auteurs(nom, prenom, nationalite) VALUES(%s, %s, %s)",
        (nom, prenom, nationalite)
    )
    connexion.commit()


# 3️Tests — exécutés SEULEMENT si on lance db.py directement
if __name__ == "__main__":
    livres = get_livres()
    for livre in livres:
        print(f"{livre[0]} - {livre[1]}")
    auteurs = get_auteurs()
    for auteur in auteurs:
        print(f"{auteur [0]} - {auteur[1]}")
