from flask import Flask, render_template, request, redirect
from db import get_livres, get_auteurs, ajouter_livre

app = Flask(__name__)

# route d'accueil
@app.route("/")
def accueil():
    return "Bienvenue dans ma bibliothèque !"

# route pour le livres
@app.route("/livres")
def liste_livres():
    livres = get_livres()
    resultat = ""
    for livre in livres:
        resultat += f"{livre[0]} - {livre[1]}<br>"
    return render_template("livres.html", livres=livres)

#route pour les auteurs
@app.route("/auteurs")
def liste_auteurs():
    auteurs = get_auteurs()
    resultat = ""
    for auteur in auteurs:
        resultat += f"{auteur[0]} - {auteur[1]}<br>"
    return render_template("auteurs.html", auteurs=auteurs )

# route pour ajouter un livre
@app.route("/ajouter_livre", methods=["GET", "POST"])
def ajouter_livre_route():
    if request.method == "POST":
        titre = request.form["titre"]
        id_auteur = request.form["id_auteur"]
        date_publication = request.form["date_publication"]
        genre = request.form["genre"]
        ajouter_livre(titre, id_auteur, date_publication, genre)
        return redirect("livres")
    return render_template("ajouter_livre.html")

if __name__ == "__main__":
    app.run(debug=True)
