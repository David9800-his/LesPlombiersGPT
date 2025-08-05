from flask import Flask, render_template, request, Response
from functools import wraps
from datetime import datetime

app = Flask(__name__, static_folder="static", template_folder="templates")

PASSWORD = "plomberie"

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.password != PASSWORD:
            return Response(
                "Accès refusé. Authentification requise.",
                401,
                {"WWW-Authenticate": 'Basic realm="Login Required"'}
            )
        return f(*args, **kwargs)
    return decorated

@app.route("/")
def index():
    return render_template("carousel.html")

@app.route("/admin")
@auth_required
def admin():
    return render_template("admin.html")

@app.route("/admin/podium", methods=["POST"])
@auth_required
def podium():
    return "Podium mis à jour!"

@app.route("/player/<nom>")
def fiche_joueur(nom):
    return render_template("fiche_joueur.html", nom=nom)

@app.route("/historique")
def historique():
    return render_template("historique.html")

@app.route("/classement")
def classement():
    return render_template("player.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
