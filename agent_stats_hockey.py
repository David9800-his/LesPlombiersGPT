from flask import Flask, render_template, request, redirect, Response
from functools import wraps
from datetime import datetime

app = Flask(__name__)

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
    return "<h1>Bienvenue chez les Plombiers 🧰🏒</h1>"

@app.route("/admin")
@auth_required
def admin():
    return render_template("admin.html")

@app.route("/admin/podium", methods=["POST"])
@auth_required
def podium():
    return "Podium mis à jour!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
