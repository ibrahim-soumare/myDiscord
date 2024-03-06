import tkinter as tk
from tkinter import scrolledtext

def envoyer_message(zone_messages, champ_message):
    message = champ_message.get()
    if message:
        zone_messages.insert(tk.END, f"Vous: {message}\n")
        champ_message.delete(0, tk.END)