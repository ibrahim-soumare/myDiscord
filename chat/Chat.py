import tkinter as tk
from tkinter import scrolledtext

def envoyer_message(zone_messages, champ_message):
    message = champ_message.get()
    if message:
        zone_messages.insert(tk.END, f"Vous: {message}\n")
        champ_message.delete(0, tk.END)

def ajouter_chat_interface(root):
    # Création de la zone de texte pour les messages
    zone_messages = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=15)
    zone_messages.grid(row=0, column=0, columnspan=2, pady=10)

    # Création de la zone de saisie pour les messages
    champ_message = tk.Entry(root, width=40)
    champ_message.grid(row=1, column=0, pady=5)