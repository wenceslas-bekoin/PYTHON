import psycopg2
from dotenv import load_dotenv
import os

from pathlib import Path

# Chemin absolu
env_path = Path("/home/bekoin-wenceslas/PYTHON/.env")
load_dotenv(dotenv_path=env_path)

#  Connexion
connexion = psycopg2.connect(
    host     = os.getenv("DB_HOST"),
    database = os.getenv("DB_NAME"),
    user     = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD")
)
curseur = connexion.cursor()

# Fonctions lire les livres
def get_livres():
    """Récupérer tous les livres"""
    curseur.execute("SELECT titre, genre FROM livres")
    return curseur.fetchall()

# Fonction ajouter un livre
def ajouter_livre(titre, id_auteur, date_publication, genre):
    """Ajouter un livre"""
    curseur.execute(
        "INSERT INTO livres(titre, id_auteur, date_publication, genre) VALUES(%s, %s, %s, %s)",
        (titre, id_auteur, date_publication, genre)
    )
    connexion.commit()

# fonction lire les auteurs
def get_auteurs():
    """Récupérer tous les auteurs"""
    curseur.execute("SELECT nom, prenom, nationalite FROM auteurs")
    return curseur.fetchall()

# Fonction ajouter auteur
def ajouter_auteur(nom, prenom, nationalite):
    """Ajouter un auteur"""
    curseur.execute(
        "INSERT INTO auteurs(nom, prenom, nationalite) VALUES(%s, %s, %s)",
        (nom, prenom, nationalite)
    )
    connexion.commit()

# Fonction lire les membres
def get_membres():
    """Récupérer tous les membres"""
    curseur.execute("SELECT  nom, prenom, email, date_inscription FROM membres")
    return curseur.fetchall()

# Fonction ajouter un membre
def ajouter_membre(nom, prenom, email, date_inscription):
    """Ajouter un membre"""
    curseur.execute(
        "INSERT INTO membres(nom, prenom, email, date_inscription) VALUES(%s, %s, %s, %s)",
        (nom, prenom, email, date_inscription)
    )
    connexion.commit()

# fonction récupérer tous les emprunts
def get_emprunts():
    """Voir tous les emprunts"""
    curseur.execute("SELECT id_membre, id_livre, date_emprunt, "
                    "date_retour_prevue, date_retour_effective FROM emprunts")
    return curseur.fetchall()


# 3️Tests — exécutés seulement si on lance db.py directement
if __name__ == "__main__":
    livres = get_livres()
    for livre in livres:
        print(f"{livre[0]} - {livre[1]}")
    auteurs = get_auteurs()
    for auteur in auteurs:
        print(f"{auteur [0]} - {auteur[1]}- {auteur[2]}")
