const bouton = document.querySelector("#afficher-site");
const liste = document.querySelector("#sites-liste");

bouton.addEventListener("click", function(){
    liste.classList.toggle("cachee");
});