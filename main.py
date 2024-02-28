import tkinter as tk

# Fonction pour afficher un message dans la console
def afficher_message():
    print("Message affiché")

# Fonction pour afficher la fenêtre d'inscription
def afficher_fenetre_inscription():
    # Création de la fenêtre d'inscription
    fenetre_inscription = tk.Toplevel(root)
    fenetre_inscription.title("Inscription")
    fenetre_inscription.geometry("400x300")  # Définition de la taille de la fenêtre

   
    # Changer le fond en noir et l'écriture en blanc pour la fenêtre d'inscription
    fenetre_inscription.configure(bg="black")

    # Labels et champs d'entrée pour l'inscription
    etiquette_prenom = tk.Label(fenetre_inscription, text="Prénom:", bg="black", fg="white")
    etiquette_prenom.grid(row=0, column=0, padx=5, pady=5)

    champ_prenom = tk.Entry(fenetre_inscription)
    champ_prenom.grid(row=0, column=1, padx=5, pady=5)

    etiquette_nom = tk.Label(fenetre_inscription, text="Nom:", bg="black", fg="white")
    etiquette_nom.grid(row=1, column=0, padx=5, pady=5)

    champ_nom = tk.Entry(fenetre_inscription)
    champ_nom.grid(row=1, column=1, padx=5, pady=5)

    etiquette_email = tk.Label(fenetre_inscription, text="E-mail:", bg="black", fg="white")
    etiquette_email.grid(row=2, column=0, padx=5, pady=5)

    champ_email = tk.Entry(fenetre_inscription)
    champ_email.grid(row=2, column=1, padx=5, pady=5)

    etiquette_mot_de_passe_inscription = tk.Label(fenetre_inscription, text="Mot de passe:", bg="black", fg="white")
    etiquette_mot_de_passe_inscription.grid(row=3, column=0, padx=5, pady=5)

    champ_mot_de_passe_inscription = tk.Entry(fenetre_inscription, show="*")
    champ_mot_de_passe_inscription.grid(row=3, column=1, padx=5, pady=5)

    bouton_inscription = tk.Button(fenetre_inscription, text="S'inscrire", command=afficher_message, bg="black", fg="white")
    bouton_inscription.grid(row=4, column=0, columnspan=2, pady=5)



# Création de la fenêtre principale
root = tk.Tk()
root.title("My Discord")
root.geometry("800x490")  # Définition de la taille de la fenêtre principale

# Création d'un Canvas pour l'image de fond
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Chargement de l'image de fond
image_fond = tk.PhotoImage(file="fond_discord.png")
canvas.create_image(0, 0, anchor=tk.NW, image=image_fond)

# Interface pour visualiser les messages
cadre_messages = tk.Frame(canvas, bg="grey")
cadre_messages.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Interface de connexion
cadre_connexion = tk.Frame(cadre_messages, bg="grey")
cadre_connexion.grid(row=2, columnspan=2, pady=10)

etiquette_nom_utilisateur = tk.Label(cadre_connexion, text="Nom d'utilisateur ", bg="grey", fg="white")
etiquette_nom_utilisateur.grid(row=0, column=0, sticky="w")

champ_nom_utilisateur = tk.Entry(cadre_connexion)
champ_nom_utilisateur.grid(row=0, column=1)

etiquette_mot_de_passe = tk.Label(cadre_connexion, text="Mot de passe ", bg="grey", fg="white")
etiquette_mot_de_passe.grid(row=1, column=0, sticky="w")

champ_mot_de_passe = tk.Entry(cadre_connexion, show="*")
champ_mot_de_passe.grid(row=1, column=1)

bouton_connexion = tk.Button(cadre_connexion, text="Se connecter", command=afficher_message, bg="grey", fg="white")
bouton_connexion.grid(row=2, column=0, columnspan=2, pady=5)

# Bouton pour afficher la fenêtre d'inscription
bouton_inscription = tk.Button(cadre_connexion, text="S'inscrire", command=afficher_fenetre_inscription, bg="grey", fg="white")
bouton_inscription.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()

