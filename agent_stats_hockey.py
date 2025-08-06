import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html")

@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=True)

