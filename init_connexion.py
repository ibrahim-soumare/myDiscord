from logging import root
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