from flask import Flask, render_template, request, redirect
from db import get_livres, get_auteurs, ajouter_livre, ajouter_auteur, ajouter_membre, get_membres, get_emprunts
from flask import jsonify

app = Flask(__name__)

# route d'accueil
@app.route("/")
def accueil():
    return render_template("accueil.html")

# route pour les livres
@app.route("/livres")
def liste_livres():
    livres = get_livres()
    resultat = ""
    for livre in livres:
        resultat += f"{livre[0]} - {livre[1]}<br>"
    return render_template("livres.html", livres=livres)

@app.route("/api/livres")
def api_livres():
    livres = get_livres()
    resultat = []
    for livre in livres:
        resultat.append({"titre": livre[0], "genre": livre[1]})
    return jsonify(resultat)

#route pour les auteurs
@app.route("/auteurs")
def liste_auteurs():
    auteurs = get_auteurs()
    resultat = ""
    for auteur in auteurs:
        resultat += f"{auteur[0]} - {auteur[1]} -{auteur[2]}<br>"
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

# route pour ajouter un auteur
@app.route("/ajouter_auteur", methods=["GET", "POST"])
def ajouter_auteur_route():
    if request.method == "POST":
        nom = request.form["nom"]
        prenom = request.form["prenom"]
        nationalite = request.form["nationalite"]
        ajouter_auteur(nom, prenom, nationalite)
        return redirect("auteurs")
    return render_template("ajouter_auteur.html")

# route pour les membres
@app.route("/membres")
def liste_membres():
    membres = get_membres()
    resultat = ""
    for membre in membres:
        resultat +=  f"{membre[0]} - {membre[1]} -{membre[2]} - {membre[3]}<br>"
    return render_template("membres.html", membres=membres)

# route pour ajouter un membre
@app.route("/ajouter_membre", methods=["GET", "POST"])
def ajouter_membre_route():
    if request.method == "POST":
        nom = request.form["nom"]
        prenom = request.form["prenom"]
        email = request.form["email"]
        date_inscription = request.form["date_inscription"]
        ajouter_membre(nom, prenom, email, date_inscription)
        return redirect("membres")
    return render_template("ajouter_membre.html")

# route pour les emprunts
@app.route("/emprunts")
def liste_emprunts():
    emprunts = get_emprunts()
    resultat = ""
    for emprunt in emprunts:
        resultat += f"{emprunt[0]} - {emprunt[1]} - {emprunt[2]} - {emprunt[3]} - {emprunt[4]} <br>"
    return render_template("emprunts.html", emprunts=emprunts)
    
# route à propos
@app.route('/apropos')
def apropos():
    return render_template('apropos.html')

# route erreur 404
@app.errorhandler(404)
def page_introuvable():
    return render_template("404.html"), 404

# route 500
@app.errorhandler(500)
def erreur_interne():
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
